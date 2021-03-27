from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q  # Used to generate a search query 
from django.db.models.functions import Lower

from .models import Adventure, Category
from .forms import AdventurePackageForm


# Create your views here.

def all_adventures(request):
    """ A view to return the adventures listview page, includeing sorting and searching """

    adventures = Adventure.objects.all()
    query = None
    categories = None
 
    if 'category' in request.GET:
        categories = request.GET['category'].split(',')
        adventures = adventures.filter(category__name__in=categories)
        categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('adventures'))
           
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(adventure_location__location_name__icontains=query)
            adventures = adventures.filter(queries)

    context = {
        'adventures': adventures,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'adventures/adventures.html', context)

def adventure_detail(request, adventure_id):
    """ A view to return an individual adventure detail page """

    adventure = get_object_or_404(Adventure, pk=adventure_id)

    context = {
        'adventure': adventure,
    }

    return render(request, 'adventures/adventure_detail.html', context)


def add_adventure_package(request):
    """ Add an adventure to the site """
    if request.method == 'POST':
        form = AdventurePackageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added adventure package!')
            return redirect(reverse('add_adventure_package'))
        else:
            messages.error(request, 'Failed to add adventure package. Please ensure the form is valid.')
    else:
        form = AdventurePackageForm()
    
    template = 'adventures/add_adventure_package.html'
    context = {
        'form': form,
    }

    return render(request, template, context)