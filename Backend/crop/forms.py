from django import forms
from .models import Crop





class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = '__all__'

        

