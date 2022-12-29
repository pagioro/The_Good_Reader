from django.shortcuts import render
from .models import Contact

def get_contact(request):
    """ Contact form view """

    contact = Contact.objects.all()   
    
    context = {
        'contact': contact,
    }

    return render(request, 'contact/contact.html', context)
