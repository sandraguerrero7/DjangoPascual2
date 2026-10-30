from django.urls import path
from Academica import views

urlpatterns = [
    path('', views.listaFacultades, name ='listaFacultades')
]