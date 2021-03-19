from django.shortcuts import render, get_object_or_404
from .models import Adventure


# Create your views here.

def all_adventures(request):
    """ A view to return the adventures listview page, includeing sorting and searching """

    adventures = Adventure.objects.all()

    context = {
        'adventures': adventures,
    }

    return render(request, 'adventures/adventures.html', context)

def adventure_detail(request, adventure_id):
    """ A view to return an individual adventure detail page """

    adventure = get_object_or_404(Adventure, pk=adventure_id)

    context = {
        'adventure': adventure,
    }

    return render(request, 'adventures/adventure_detail.html', context)