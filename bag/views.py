from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from adventures.models import Adventure

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified adventure to the shopping bag """

    adventure = get_object_or_404(Adventure, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Added {adventure.name} to your bag')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {adventure.name} to your bag')

    request.session['bag'] = bag
    # print(request.session['bag'])
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified adventure package to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    
    if request.POST:
        bag = request.session.get('bag', {})

        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        if request.POST:
            bag = request.session.get('bag', {})
            del bag[item_id]
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
    