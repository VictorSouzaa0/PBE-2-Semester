from django import forms
from django.forms import ModelForm
from .models import Everthing

class EverForm(forms.ModelForm):
    class Meta:
        model = Everthing
        fields = ['name',]