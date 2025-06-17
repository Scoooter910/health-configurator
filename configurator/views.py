from django.shortcuts import render, redirect
from .forms import HealthConfigForm
from .forms import HealthConfigForm, CSVUploadForm


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

import pandas as pd

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']

            try:
                df = pd.read_csv(csv_file)
                print("📊 Data Preview:")
                print(df.head())  # Optional: output to terminal
                summary = df.describe(include='all').to_html()
                return render(request, 'csv_result.html', {'summary': summary})
            except Exception as e:
                return render(request, 'upload_csv.html', {'form': form, 'error': str(e)})

    else:
        form = CSVUploadForm()

    return render(request, 'upload_csv.html', {'form': form})
