from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes,parser_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .models import userAbs
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def create_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    bio = request.data.get('bio')
    age = request.data.get('age')
    phone = request.data.get('phone')

    if not username or not password or not bio or not age or not phone:
        return Response({"Erro":"Informações insuficientes"},status=status.HTTP_400_BAD_REQUEST)
    
    if userAbs.objects.filter(username=username).exists():
        return Response({"Erro":"Esse usuário ja é existente"},status=status.HTTP_400_BAD_REQUEST)
    
    if userAbs.objects.filter(phone=phone).exists():
        return Response({"Erro":"Númeo não existente"},status=status.HTTP_400_BAD_REQUEST)
    
    user = userAbs.objects.create_user(
        username=username,
        password=password,
        bio=bio,
        age=age,
        phone=phone
    )
    return Response({"Mensagem":f"Usuário {username} criado com sucesso!!"},status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login(request):
    username =  request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user:
        refresh = RefreshToken.for_user(user)

        return Response({
            'Access': str(refresh.access_token),
            'Refreseh': str(refresh)
        },status=status.HTTP_200_OK)
    else:
        return Response({"Erro":"Usuário ou senha incorretos"}, status=status.HTTP_401_UNAUTHORIZED)
    