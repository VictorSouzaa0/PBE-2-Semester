from django.urls import path
from . import views

urlpatterns = [
    path('create/',view=views.create_user),
]
