#lista inicial de tarefas
minhas_tarefas = ["Estudar python", "Fazer exames", "Comprar pão", "Revisar matéria"]
print( f"Tarefas pendentes: {minhas_tarefas}")

# Adicionando uma nova tarefa ao final da lista 
minhas_tarefas.append ("Lavar a louça")
print(f"Tarefa adicinando: {minhas_tarefas}")

#Adicionando uma tarefa em uma posição específica (índice 1)

minhas_tarefas.insert(1, "Responder e-mails")
print(f"Tarefa inserida em posição específica: {minhas_tarefas}")

#Removendo uma tarefa que já foi feita (pelo nome )
minhas_tarefas.remove("Comprar pão")
print(f"Tarefa 'comprar pão' removida:{minhas_tarefas}")

#removendo a última tarefa
tarefa_removida = minhas_tarefas.pop() #remove "revisar matéria"
print(f"Última tarefa removida('{tarefa_removida}'):{minhas_tarefas}")