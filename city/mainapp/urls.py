from django.urls import include, path

from .views import *


urlpatterns = [
    path('city/<int:city_id>', city, name='current_city'),
    path('', index),
]
