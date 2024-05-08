"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crop.views import crop_predict
from chest_x_ray.views import detect_x_ray
from chest_x_ray.api import Detect_X_RayAPI

from crop.api import PredictAPI
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crop/', crop_predict, name='crop_predict'),
    path('x-ray/', detect_x_ray, name='x-ray'),

    path('api/v1/crop/',PredictAPI.as_view() , name='crop_predict_api'),
    path('api/v1/chest/',Detect_X_RayAPI.as_view() , name='detect_x_ray'),


]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)