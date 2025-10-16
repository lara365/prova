from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_projetos, name='lista_projeto'),#seria/projeto/
   
    ]
