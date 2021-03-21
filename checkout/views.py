from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('adventures'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IXR2ACmrnzo0YOhMPpxBMCh0MN6dYrSIhDDoO9FTy4vtlTCd3quy9AlVVSbgMhbWpoQ8WQuKMCeXTAZmqwV4y5m003EfpUwR5',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
