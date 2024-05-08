from rest_framework import generics,status
from rest_framework.response import Response
from .models import Crop
import joblib
import pandas as pd

class PredictAPI(generics.GenericAPIView):

    def post(self,request,*args, **kwargs):
        payload = request.data
        nitrogen= payload['nitrogen']
        phosphorus= payload['phosphorus']
        potassium= payload['potassium']
        temperature= payload['temperature']
        humidity= payload['humidity']
        ph= payload['ph']
        rainfall= payload['rainfall']

        values=[nitrogen,phosphorus,potassium,temperature,humidity,ph,rainfall]
            
        model = joblib.load('model_1.4.2.pkl')
        result = model.predict([values])
        prediction_result = result[0]

        Crop.objects.create(

            nitrogen=nitrogen,
            phosphorus=phosphorus,
            potassium=potassium,
            temperature=temperature,
            humidity=humidity,
            ph=ph,
            rainfall=rainfall,
            prediction_result=prediction_result,


        )
        return Response({'message': "Predicted Successfully", "result":prediction_result}, status=status.HTTP_200_OK)
