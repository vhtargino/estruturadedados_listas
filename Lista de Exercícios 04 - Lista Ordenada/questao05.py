# Implemente uma função que aceite um vetor de números inteiros e remova todos
# os elementos duplicados, retornando o vetor resultante sem duplicatas.

def remover_repetidos(lista):
    nova_lista = []
    for i in lista:
        if i not in nova_lista:
            nova_lista.append(i)
    return nova_lista


lista = [11, 3, 11, 1, 11, 2, 11, 6, 11]

print(lista)
print(remover_repetidos(lista))
