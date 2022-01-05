from django.db import models
from django.contrib.auth.models import AbstractUser


class Empresa(models.Model):
    nome = models.CharField(max_length=50)
    cnpj = models.IntegerField(unique=True)

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    titulo = models.CharField(max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Usuario(AbstractUser):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)
