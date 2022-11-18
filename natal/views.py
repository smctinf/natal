from django.shortcuts import render

from natal.models import *

# Create your views here.


def index(req):
    import datetime

    programacao_=Programacao.objects.all()
    datas=programacao_.values('hora')

    index=[]
    for data in datas:
        index.append(str(data['hora'].date()))
    index=list(dict.fromkeys(index))

    programacao=[]
    for i in index:
        programacao.append([datetime.datetime.strptime(i, '%Y-%m-%d'), []])
    for p in programacao_:           
        for i in programacao:            
            if str(p.hora.date()) == str(i[0].date()):
                i[1].append(p)    
        
    # for in
    context = {
        'programacao': programacao,
        'parceiros': Parceiro.objects.all(),
        'eventos': Evento.objects.all(),
        'testemonios': Testemunho.objects.all(),
        'galeria_images': Galeria.objects.all(),
        # 'texto' :
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
