from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required
def add_adventure_package(request):
    """ Add an adventure to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AdventurePackageForm(request.POST, request.FILES)
        if form.is_valid():
            adventure = form.save()
            messages.success(request, 'Successfully added adventure package!')
            return redirect(reverse('adventure_detail', args=[adventure.id]))
        else:
            messages.error(request, 'Failed to add adventure package. Please ensure the form is valid.')
    else:
        form = AdventurePackageForm()
        
    template = 'adventures/add_adventure_package.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_adventure_package(request, adventure_id):
    """ Edit an adventure on the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    adventure = get_object_or_404(Adventure, pk=adventure_id)
    if request.method == 'POST':
        form = AdventurePackageForm(request.POST, request.FILES, instance=adventure)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated adventure!')
            return redirect(reverse('adventure_detail', args=[adventure.id]))
        else:
            messages.error(request, 'Failed to update adventure. Please ensure the form is valid.')
    else:
        form = AdventurePackageForm(instance=adventure)
        messages.info(request, f'You are editing {adventure.name}')

    template = 'adventures/edit_adventure_package.html'
    context = {
        'form': form,
        'adventure': adventure,
    }

    return render(request, template, context)


@login_required
def delete_adventure_package(request, adventure_id):
    """ Delete a adventure from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    adventure = get_object_or_404(Adventure, pk=adventure_id)
    adventure.delete()
    messages.success(request, 'Adventure package deleted!')
    return redirect(reverse('adventures'))