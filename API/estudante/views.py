from django.shortcuts import render
from .models import Aluno
from rest_framework.response import Response
from .serializers import AlunosSerializer
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def listar_alunos(request):
    alunos = Aluno.objects.all()
    serializer = AlunosSerializer(alunos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def criar_alunos(reqeust):
    if reqeust.method == 'POST':
        serializer = AlunosSerializer(data=reqeust.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)