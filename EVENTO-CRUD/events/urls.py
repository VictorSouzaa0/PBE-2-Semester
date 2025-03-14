from django.urls import path
from . import views

urlpatterns = [
    path('',views.todos_eventos),
    path('filtrar/<int:pk>',views.evento_selecionado),
    path('editar/<int:pk>',views.editar_evento),
]
