from tabnanny import verbose
from tkinter import CASCADE, image_names
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Parceiro(models.Model):
    nome=models.CharField(max_length=30, verbose_name="Nome do parceiro")
    logo=models.ImageField(upload_to='parceiros_logos', verbose_name="Imagem para logo do parceiro") 
    site=models.CharField(verbose_name="URL do site do parceiro", max_length=50, null=True)

class Evento(models.Model):
    titulo=models.CharField(max_length=50, verbose_name="Título do evento")
    banner=models.ImageField(upload_to='eventos_banners', verbose_name="Banner para divulgação do evento")
    data=models.DateField(auto_now=False, auto_now_add=False) 
    descricao=models.TextField(max_length=150)

class Testemunho(models.Model):
    autor=models.CharField(max_length=50, verbose_name="Nome da pessoa")
    comentario=models.TextField(max_length=150) 

class Galeria(models.Model):
    image = models.ImageField(upload_to='galerias_imagens', verbose_name="Imagem da galeria")
    user = models.ForeignKey(User, on_delete=models.CASCADE)