from rest_framework import generics,status
from rest_framework.response import Response
from .models import Chest_x_ray
from keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
import joblib
import pandas as pd
import io
import base64
from PIL import Image
from io import BytesIO






def preprocess_image(image_data, img_dim):
    # Decode base64 encoded image data
    decoded_image = base64.b64decode(image_data.split(',')[1])
    
    # Open the image using PIL (Python Imaging Library)
    img = Image.open(BytesIO(decoded_image))
    
    # Resize the image to the desired dimensions
    img = img.resize((img_dim, img_dim))
    
    # Convert the image to a numpy array
    img_array = np.array(img)
    
    # Check if the image is grayscale and convert it to RGB if necessary
    if len(img_array.shape) == 2:
        img_array = np.stack((img_array,) * 3, axis=-1)
    
    # Ensure the image has 3 color channels (RGB)
    if img_array.shape[2] != 3:
        raise ValueError("Input image should have 3 color channels (RGB)")
    
    # Reshape the image array to match the required input shape
    preprocessed_image = img_array.reshape(1, img_dim, img_dim, 3)
    
    # Normalize the pixel values
    preprocessed_image = preprocessed_image / 255.0
    
    return preprocessed_image







class Detect_X_RayAPI(generics.GenericAPIView):

    def post(self,request,*args, **kwargs):
        payload = request.data

        image_data= payload['image']
        #image_bytes = io.BytesIO(image_data.read())
            
        # Preprocess the image
        preprocessed_image = preprocess_image(image_data, 150)
    
        model = load_model('detect.h5')

        prediction = model.predict(preprocessed_image)

        # Interpret predictions
        predicted_label = "NORMAL" if prediction < 0.5 else "PNEUMONIA"

              
        Chest_x_ray.objects.create(image=image_data,result_pred=predicted_label)
       
        return Response({'message': "Detected Successfully", "result":predicted_label}, status=status.HTTP_200_OK)
