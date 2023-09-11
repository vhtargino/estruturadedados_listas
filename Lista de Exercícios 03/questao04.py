def ordenar(lista):
    for i in range(len(lista)):
        indice_minimo = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]


def segundo_menor(lista):
    ordenar(lista)
    return lista[1]


lista = [11, 3, 8, 9, 1, 7, 12, 2, 5, 13, 6, 10, 4]

ordenar(lista)
print(segundo_menor(lista))
