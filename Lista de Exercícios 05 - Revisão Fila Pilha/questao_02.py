# 2. Você está desenvolvendo um sistema de fila de atendimento para um banco.
# Os clientes entram na fila e são atendidos pelos funcionários na ordem de chegada.
# Use a classe de fila para simular o atendimento dos clientes.

from fila import Fila
import time

def atender_cliente(fila_atendimento):
    while not fila_atendimento.fila_vazia():
        cliente_atual = fila_atendimento.desenfileirar()
        print(f"Atendendo cliente: {cliente_atual}")
        time.sleep(1)


def simular_atendimento_banco(capacidade, num): # Capacidade da fila e número de clientes a serem atendidos
    fila_atendimento = Fila(capacidade)

    for i in range(num):
        fila_atendimento.enfileirar(f"Cliente-{i}")

    print("Fila antes do atendimento:")
    fila_atendimento.visualizar()

    print("\nIniciando atendimento...\n")
    atender_cliente(fila_atendimento)

    print("\nFila após o atendimento:")
    fila_atendimento.visualizar()


simular_atendimento_banco(5, 3)
