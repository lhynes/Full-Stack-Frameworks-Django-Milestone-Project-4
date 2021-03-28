from django.shortcuts import render

from adventures.models import Adventure

# Create your views here.

def index(request):
    """ A view to return the index page  and show adventures"""
    
    return render(request, 'home/index.html')


def show_adventures(request):
    """ A view to load the home page with adventures """
    
    show_adventures = Adventure.objects.all()

    context = {
       'show_adventures': show_adventures,
    }
   
    # show_adventures is to loop adventures on the home page.
    return render(request, 'home/index.html', context)