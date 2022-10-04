from django.shortcuts import render

from natal.models import *

# Create your views here.


def index(req):
    context = {
        'parceiros': Parceiro.objects.all(),
        'eventos': Evento.objects.all(),
        'testemonios': Testemunho.objects.all(),
        'galeria_images': Galeria.objects.all(),
    }

    return render(req, "natal/index.html", context)


def sobre(req):
    context = {
        'parceiros': Parceiro.objects.all(),
    }
    return render(req, "natal/sobre.html", context)


def casaDoPapaiNoel(req):
    context = {
        'parceiros': Parceiro.objects.all(),
    }
    return render(req, "natal/casaDoPapaiNoel.html", context)
