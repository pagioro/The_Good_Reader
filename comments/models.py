from django.db import models
# from django.contrib.auth.models import User
# from django_summernote.fields import SummernoteTextField
# from django.template.defaultfilters import slugify
# from cloudinary.models import CloudinaryField
# # from django.core.validators import MaxValueValidator, MinValueValidator

class Comment(models.Model):
    """
    Model for comment
    """
    id_comment = models.AutoField(primary_key=True)
    id_product = models.PrimaryKey('Product', null=True, blank=True, on_delete=models.SET_NULL)
    id_user = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=80)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField() 
    approved = models.BooleanField(default=False)


# class Meta:
#     """
#     Orders the comments in ascending order
#     """
#     ordering = ['-created_date']

#     def __str__(self):
#         return f"Comment {self.content} by {self.name}"