from django.contrib import admin
from .models import Bugreport


class BugreportAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


admin.site.register(Bugreport, BugreportAdmin)
