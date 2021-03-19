from django.shortcuts import render
from .models import Adventure


# Create your views here.

def all_adventures(request):
    """ A view to return the adventures listview page, includeing sorting and searching """

    adventures = Adventure.objects.all()

    context = {
        'adventures': adventures,
    }

    return render(request, 'adventures/adventures.html',context)