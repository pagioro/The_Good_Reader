from django.shortcuts import render
from .models import Contact

def get_contact(request):
    """ A view to show all products, including sorting and search queries """

    contact = Contact.objects.all()   
    
    context = {
        'contact': contact,
    }

    return render(request, 'contact/contact.html', context)
