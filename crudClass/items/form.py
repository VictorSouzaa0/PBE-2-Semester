from django import forms
from .models import *

class ItemCar(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'