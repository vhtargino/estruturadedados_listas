# 4. Você está criando um aplicativo de lista de tarefas pendentes.
# As tarefas são adicionadas à fila e concluídas uma por uma.
# Use a classe de fila para implementar a lista de tarefas e concluir as tarefas na ordem em que foram adicionadas.

from fila import Fila
import time

def concluir_tarefas(fila_tarefas):
    while not fila_tarefas.fila_vazia():
        tarefa_atual = fila_tarefas.desenfileirar()
        print(f"Concluindo tarefa: {tarefa_atual}")
        time.sleep(1)


def simular_lista_tarefas(capacidade, array_tarefas):
    fila_tarefas = Fila(capacidade)

    for tarefa in array_tarefas:
        fila_tarefas.enfileirar(tarefa)

    print("Lista de tarefas pendentes:")
    fila_tarefas.visualizar()

    print("\nConcluindo tarefas...\n")
    concluir_tarefas(fila_tarefas)

    print("\nLista de tarefas após conclusão:")
    fila_tarefas.visualizar()


tarefas = ["Comer", "Fazer exercícios", "Tirar o lixo", "Varrer"]
simular_lista_tarefas(5, tarefas)
