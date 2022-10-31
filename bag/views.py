from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from bookings.models import Booking

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified items to the shopping bag """

    booking = Booking.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {booking.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    """ Update the quantity of specific item to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] += quantity
    else:
        bag.pop(item_bag)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


# def remove_from_bag(request, item_id):
#     """ Remove the item from the shopping bag """

#     try:
#         booking = get_object_or_404(Booking, pk=item_id)
#         bag = request.session.get('bag', {})

#         else:
#             bag.pop(item_bag)
#             messages.success(request, f'Removed {booking.name} from your bag')

#         request.session['bag'] = bag
#         return HttpResponse(status=200)
    
#     except Exception as e:
#         messages.error(request, f'Error removing item: {e}')
#         return HttpResponse(status=500)