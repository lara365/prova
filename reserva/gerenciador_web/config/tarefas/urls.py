from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tarefas, name='lista_tarefas'),#seria/tarefa/
    path('<int:tarefa_id>/', views.detalhe_tarefa, name='detalhe_tarefa'),
    #adicionar tarefas
    path('adicionar/', views.adicionar_tarefa,name = 'adicionar_tarefa'),
    ]

