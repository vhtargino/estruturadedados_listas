# Crie uma função que aceite um vetor de números inteiros e retorne o terceiro maior número.
# Certifique-se de que sua função funcione mesmo se houver números duplicados no vetor.

def ordenar(lista):
    for i in range(len(lista)):
        indice_minimo = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]


def terceiro_menor(lista):
    ordenar(lista)
    return lista[2]


lista = [11, 3, 8, 9, 1, 7, 12, 2, 5, 13, 6, 10, 4]

ordenar(lista)
print(terceiro_menor(lista))
