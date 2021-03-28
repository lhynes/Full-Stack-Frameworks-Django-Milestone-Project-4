from django.shortcuts import render


def about(request):
    """ A view to return the company about page """

    return render(request, 'about/about.html')