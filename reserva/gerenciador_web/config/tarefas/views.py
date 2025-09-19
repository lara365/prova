from django.shortcuts import render

# Create your views here.

from .models import Tarefa
from django.http import HttpResponse

def listar_tarefas(request):
    #1 a busca no banco de dados continua a mesma
    tarefas_salvas = Tarefa.objects.all()
    #2 criamos um  dicionario de contexto para enviar os dados ao template
    #a chave 'minhas_tarefas',será a variavel que usamos no html 
    contexto = {
        'minhas_tarefas': tarefas_salvas
    }


#3. renderizamos o template , passando a requesição e o contexto com os dados. 
    return render(request, 'tarefas/lista.html', contexto)


