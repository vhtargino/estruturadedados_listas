# 1. Você está desenvolvendo um sistema de fila de impressão para uma empresa.
# Os documentos são adicionados à fila e impressos na ordem em que foram recebidos.
# Implemente um programa Python que use a classe de fila para simular esse processo.

from fila import Fila
import time

def imprimir_documento(documento):
    print(f"Imprimindo documento: {documento}")
    time.sleep(1)


def simulador_fila_impressao(capacidade, num): # Capacidade da fila e número de documentos a serem impressos
    fila_impressao = Fila(capacidade)

    for i in range(num):
        fila_impressao.enfileirar(f"Documento-{i}")

    print("Fila antes da impressão:")
    fila_impressao.visualizar()

    print("\nIniciando impressão...\n")
    while not fila_impressao.fila_vazia():
        documento_atual = fila_impressao.desenfileirar()
        imprimir_documento(documento_atual)

    print("\nFila após a impressão:")
    fila_impressao.visualizar()


simulador_fila_impressao(10, 5)
