from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Booking, Category
from .forms import BookingForm

# Create your views here.

def all_bookings(request):
    """ A view to show all bookings, including sorting and search queries """

    bookings = Booking.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                bookings = bookings.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                bookings = bookings.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            bookings = bookings.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('bookings'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            bookings = bookings.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'bookings': bookings,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'bookings/bookings.html', context)


def booking_detail(request, booking_id):
    """ A view to show individual booking details """

    booking = get_object_or_404(Booking, pk=booking_id)

    context = {
        'booking': booking,
    }

    return render(request, 'bookings/booking_detail.html', context)


def add_booking(request):
    """ Add a booking to the Bookings page """
    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added booking!')
            return redirect(reverse('add_booking'))
        else:
            messages.error(request, 'Failed to add booking. Please ensure the form is valid.')
    else:
        form = BookingForm()

    template = 'bookings/add_booking.html'
    context = {
        'form': form,
    }

    return render(request, template, context)