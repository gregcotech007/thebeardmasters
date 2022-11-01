from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('bookings'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Lz9hiA70jm9huLLDpZbcPhOB1DE4hgJTR8jfgoVvSwASwlaZbKJOf8hXD9aMH1ht9sw0B5FXMblhkvBArVKqlYr00ll9urqEn',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
