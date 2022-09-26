
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('natal/', views.index),
    path('sobre/', views.sobre),
    path('casaDoPapaiNoel/', views.casaDoPapaiNoel),

]
