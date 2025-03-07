from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    idade = models.PositiveIntegerField()
    curso = models.CharField(max_length=50)
    instituicao = models.CharField(max_length=100)
    rm = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.rm}--{self.nome}"
    class Meta:
        verbose_name_plural = "Alunos"