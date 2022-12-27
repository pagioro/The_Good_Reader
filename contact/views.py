from django.shortcuts import render
from .models import Contact

def get_authors(request):
    """ A view to show all products, including sorting and search queries """

    contact = Contact.objects.all()   
    
    context = {
        'contacts': contact,
    }

    return render(request, 'contact/contact.html', context)
