from django.shortcuts import render
from .models import Contact
from .forms import CommentForm

def get_contact(request):
    """ Contact form view """

    contact = Contact.objects.all()  
    print(contact, "get_contact contact var") 
    
    context = {
        'contact': contact,
        'comment_form': CommentForm(),
    }

    return render(request, 'contact/contact.html', context)

