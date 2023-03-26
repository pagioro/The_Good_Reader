from django.shortcuts import render
from .models import Contact
from .forms import ContactForm


def get_contact(request):
    """ Contact form view """

    contact = Contact.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'contact': contact,
        'contact_form': ContactForm(),
    }

    return render(request, 'contact/contact.html', context)
