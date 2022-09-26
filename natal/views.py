from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, "natal/index.html")
    
def sobre(req):
    return render(req, "natal/sobre.html")

def casaDoPapaiNoel(req):
    return render(req, "natal/casaDoPapaiNoel.html")