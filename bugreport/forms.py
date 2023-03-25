from .models import Bugreport
from django import forms


class BugreportForm(forms.ModelForm):
    """
    Bug Report form
    """
    class Meta:
        model = Bugreport
        fields = [
            'title',
            'description',            
            'browser',
            'os',
            'email',
        ]