from django.db import models

# Create your models here.









class Chest_x_ray(models.Model):
    image = models.ImageField(upload_to='x_ray')
    result_pred = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.result_pred