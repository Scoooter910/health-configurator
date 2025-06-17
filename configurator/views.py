from django.shortcuts import render, redirect
from .forms import HealthConfigForm

def config_form(request):
    if request.method == 'POST':
        form = HealthConfigForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HealthConfigForm()
    return render(request, 'config_form.html', {'form': form})

def success_page(request):
    return render(request, 'success.html')
