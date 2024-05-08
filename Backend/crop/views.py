from django.http import HttpResponse
from django.shortcuts import render
from .models import Crop
from .forms import CropForm
import joblib
import pandas as pd



def crop_predict(request):
    if request.method == 'POST':
        form = CropForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)

            nitrogen= form.cleaned_data['nitrogen']
            phosphorus= form.cleaned_data['phosphorus']
            potassium= form.cleaned_data['potassium']
            temperature= form.cleaned_data['temperature']
            humidity= form.cleaned_data['humidity']
            ph= form.cleaned_data['ph']
            rainfall= form.cleaned_data['rainfall']

            values=[nitrogen,phosphorus,potassium,temperature,humidity,ph,rainfall]


            
            model = joblib.load('model_1.4.2.pkl')
            result = model.predict([values])


            prediction_result = result[0]

            myform.prediction_result = prediction_result
            myform.save()
            return render(request,'predict.html', {'form':form, 'result':prediction_result})
    else:
        form=CropForm()     

    return render(request,'predict.html', {'form':form})       





