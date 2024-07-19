# obituaries/views.py
from django.shortcuts import render, redirect
from .models import Obituary
from .form import ObituaryForm

def submit_obituary(request):
    if request.method == 'POST':
        form = ObituaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_obituaries')
    else:
        form = ObituaryForm()
    return render(request, 'obituaries/obituary_form.html', {'form': form})

def view_obituaries(request):
    obituaries = Obituary.objects.all()
    return render(request, 'obituaries/view_obituaries.html', {'obituaries': obituaries})
