from django.http import HttpResponse
from django.shortcuts import render
from .models import Chest_x_ray
from .forms import Chest_x_rayForm
from keras.preprocessing import image
from tensorflow.keras.models import load_model
import joblib
import pandas as pd
import numpy as np
import io

# Create your views here.



def preprocess_image(image_data, img_dim):
    img = image.load_img(image_data, target_size=(img_dim, img_dim))
    img_array = image.img_to_array(img)
    preprocessed_image = img_array.reshape(1, img_dim, img_dim, 3)
    preprocessed_image = preprocessed_image / 255.0  
    return preprocessed_image



def detect_x_ray(request):
    if request.method == 'POST':
        form = Chest_x_rayForm(request.POST, request.FILES)

        if form.is_valid():
            myform = form.save(commit=False)

            image = form.cleaned_data['image']

            image_data = request.FILES['image']
            image_bytes = io.BytesIO(image_data.read())
            
            # Preprocess the image
            preprocessed_image = preprocess_image(image_bytes, 150)
        
            model = load_model('detect.h5')


            prediction = model.predict(preprocessed_image)

            # Interpret predictions
            predicted_label = "NORMAL" if prediction < 0.5 else "PNEUMONIA"


            myform.result_pred = predicted_label
            myform.save()
            return render(request,'x-ray.html', {'form':form, 'result':predicted_label})
    else:
        form=Chest_x_rayForm()     

    return render(request,'x-ray.html', {'form':form})       



