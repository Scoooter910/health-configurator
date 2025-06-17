from django import forms
from .models import HealthConfig

class HealthConfigForm(forms.ModelForm):
    class Meta:
        model = HealthConfig
        fields = '__all__'
        
from django import forms

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label='Select a CSV file')
