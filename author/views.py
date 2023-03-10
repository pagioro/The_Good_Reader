from django.shortcuts import render
from .models import Author


def get_authors(request):
    """ A view to show all products, including sorting and search queries """

    authors = Author.objects.all()

    context = {
        'authors': authors,
    }

    return render(request, 'author/author.html', context)
    
