from django import forms
from .models import Chest_x_ray




        


class Chest_x_rayForm(forms.ModelForm):
    class Meta:
        model = Chest_x_ray
        fields = '__all__'