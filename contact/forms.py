from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Contact form
    """
    class Meta:
        model = Comment
        fields = [
            'name',
            'email',            
            'title',
            'description',
        ]









    