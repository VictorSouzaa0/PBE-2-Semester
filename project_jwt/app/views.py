from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes,parser_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

from .models import UserAbs
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def create_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    cargo = request.data.get('cargo')
    telefone =  request.data.get('telefone')

    if not username or not password or not email or not cargo or not telefone:
        return Response({"Erro": "informações insuficientes"}, status=status.HTTP_400_BAD_REQUEST)
    
    if UserAbs.objects.filter(username=username).exists():
        return Response ({"Erro": "Username já existe"},status=status.HTTP_400_BAD_REQUEST)
    
    if UserAbs.objects.filter(email=email).exists():
        return Response({"ERRO": "Email ja existe"}, status=status.HTTP_400_BAD_REQUEST)
    
    user = UserAbs.objects.create_user(
        username=username,
        password=password,
        email=email,
        cargo=cargo,
        telefone=telefone,
    )
    return Response({"Mensagem":f"Usuario {username} criado com sucesso"},status=status.HTTP_201_CREATED)

@api_view(['POST'])
def loggin(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user:
        refresh = RefreshToken.for_user(user)

        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh)  
        },status=status.HTTP_200_OK)
    else:
        return Response({'Erro': 'usuario ou senha invalidos'},status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protect_view(request):
    return Response({"Mensagem": "Olá DS14"}, status=status.HTTP_201_CREATED)