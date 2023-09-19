
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.index),
    path('', views.index, name='home'),
    path('sobre/', views.sobre),
    path('casaDoPapaiNoel/', views.casaDoPapaiNoel, name="casaPapaiNoel"),
]
