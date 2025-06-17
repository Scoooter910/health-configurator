from django import forms
from .models import HealthConfig

class HealthConfigForm(forms.ModelForm):
    class Meta:
        model = HealthConfig
        fields = '__all__'
