from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Evento
from .serializers import EventoSerializers
import json

@api_view(['GET'])
def todos_eventos(request):
    if request.method == 'GET':
        eventos =  Evento.objects.all()
        serializer = EventoSerializers(eventos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

    #query params

@api_view(['GET'])

def evento_selecionado(resquet,pk):
    try:
        evento = Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = EventoSerializers(evento)
    return Response(serializer.data)
