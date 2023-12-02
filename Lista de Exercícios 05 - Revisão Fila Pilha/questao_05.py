# 5. Em um sistema de comércio eletrônico, os pedidos online são processados em uma fila.
# Implemente uma classe de fila que gerencie os pedidos online e processe-os na ordem de chegada.

from fila import Fila
import time

def pedidos_online(fila_pedidos):
    while not fila_pedidos.fila_vazia():
        tarefa_atual = fila_pedidos.desenfileirar()
        print(f"Pedido atual: {tarefa_atual}")
        time.sleep(1)


def simular_pedidos_online(capacidade, array_pedidos):
    fila_pedidos = Fila(capacidade)

    for pedido in array_pedidos:
        fila_pedidos.enfileirar(pedido)

    print("Lista de pedidos pendentes:")
    fila_pedidos.visualizar()

    print("\nProcessando pedidos...\n")
    pedidos_online(fila_pedidos)

    print("\nLista de pedidos após conclusão:")
    fila_pedidos.visualizar()


pedidos = ["Smartphone", "Smartwatch", "Cabo USB", "Carregador", "Fonte notebook"]
simular_pedidos_online(5, pedidos)
