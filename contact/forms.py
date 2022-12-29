from .models import Contact
from django import forms


class CommentForm(forms.ModelForm):
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









    