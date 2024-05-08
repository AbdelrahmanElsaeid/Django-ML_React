from django.db import models

# Create your models here.



class Crop(models.Model):
    nitrogen= models.FloatField()
    phosphorus= models.FloatField()
    potassium= models.FloatField()
    temperature= models.FloatField()
    humidity= models.FloatField()
    ph= models.FloatField()
    rainfall= models.FloatField()
    prediction_result = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.prediction_result
    

