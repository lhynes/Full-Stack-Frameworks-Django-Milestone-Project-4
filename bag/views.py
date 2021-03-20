from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ A view the renders the bacg contents page """

    return render(request, 'bag/bag.html')