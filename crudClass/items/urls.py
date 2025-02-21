from django.urls import path
from . import views

urlpatterns = [
     path('', views.car_read, name='car_create'),
     path('new/',views.car_create, name='cars-read'),
     path('edit/<int:pk>', views.car_update, name='car_update'),
     path('delete/<int:pk>', views.car_delete, name='car_delete')
]
