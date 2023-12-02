# 3. Imagine um sistema de gerenciamento de pedidos para um restaurante.
# Os pedidos dos clientes são colocados em uma fila e processados na ordem em que foram feitos.
# Use a classe de fila para gerenciar os pedidos e processá-los na ordem correta.

from fila import Fila
import time

def processar_pedidos(fila_pedidos):
    while not fila_pedidos.fila_vazia():
        pedido_atual = fila_pedidos.desenfileirar()
        print(f"Processando Pedido: {pedido_atual}")
        time.sleep(1)


def simular_gerenciamento_pedidos(capacidade, array_pedidos): # Capacidade da fila e array contendo os pedidos
    fila_pedidos = Fila(capacidade)

    # Enfileira um item do array por vez
    for pedido in array_pedidos:
        fila_pedidos.enfileirar(pedido)

    print("Fila antes do processamento:")
    fila_pedidos.visualizar()

    print("\nIniciando processamento dos pedidos...\n")
    processar_pedidos(fila_pedidos)

    print("\nFila após o processamento:")
    fila_pedidos.visualizar()


pedidos = ["Pizza Margherita", "Hambúrguer com fritas", "Pizza Calabresa", "Salada", "Frango frito"]
simular_gerenciamento_pedidos(5, pedidos)
