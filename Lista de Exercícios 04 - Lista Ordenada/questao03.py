# Escreva um programa que encontre o elemento máximo em um vetor de inteiros
# não ordenado sem usar a função `max()`. Em seguida, encontre o elemento mínimo sem usar a função `min()`.

def valor_max(lista):
    maximo = lista[0]
    for i in lista:
        if i > maximo:
            maximo = i
    return maximo


def valor_min(lista):
    minimo = lista[0]
    for i in lista:
        if i < minimo:
            minimo = i
    return minimo


def min_max(lista):
    minimo = lista[0]
    maximo = lista[0]
    for i in lista:
        if i < minimo:
            minimo = i
        if i > maximo:
            maximo = i
    return minimo, maximo


lista = [11, 3, 8, 9, 1, 7, 12, 2, 5, 13, 6, 10, 4]

print(valor_min(lista))
print(valor_max(lista))

print(min_max(lista))
