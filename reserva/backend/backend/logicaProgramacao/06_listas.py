meus_perfumes = ["La Vie Est Belle","Laguna ","Flower by Kenzo" , "212 VIP Rosé ", "Good Girl ","J'adore ","Luna Absoluta","Kaiak Aventura "]
print(f"Tarefas pendentes: {meus_perfumes}")

meus_perfumes.insert(3, "212 VIP Rosé")
meus_perfumes.insert(4, "Laguna")
print(f"Ao adicionar registros: {meus_perfumes}")

del meus_perfumes[3]
print(f"registro '3' removida: {meus_perfumes}")

registro_removido = meus_perfumes.pop()
print(f"Última perfume removida('{registro_removido}'): {meus_perfumes}")