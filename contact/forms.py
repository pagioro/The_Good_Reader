from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    """
    Contact form
    """
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',            
            'title',
            'description',
        ]









    