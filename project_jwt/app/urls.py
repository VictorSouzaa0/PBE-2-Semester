from django.urls import path
from . import views

urlpatterns = [
    path('create',view=views.create_user),
    path('login/',view=views.loggin),
    path('view/',view=views.protect_view)
]
