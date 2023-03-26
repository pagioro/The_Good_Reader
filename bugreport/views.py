from django.shortcuts import render
from .models import Bugreport
from .forms import BugreportForm


def get_bugreport(request):
    """ Bug report views """

    bugreport = Bugreport.objects.all()

    if request.method == 'POST':
        form = BugreportForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'bugreport': bugreport,
        'bugreport_form': BugreportForm(),
    }

    return render(request, 'bugreport/bugreport.html', context)
