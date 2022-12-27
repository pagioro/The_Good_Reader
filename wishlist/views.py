from django.shortcuts import render
from .models import Wishlist

def get_wishlist(request):
    """ A view to show all products, including sorting and search queries """

    authors = Wishlist.objects.all()   
    
    context = {
        'wishlist': wishlist,
    }

    return render(request, 'wishlist/wishlist.html', context)
