def remover_repetidos(lista):
    nova_lista = []
    for i in lista:
        if i not in nova_lista:
            nova_lista.append(i)
    return nova_lista


lista = [11, 3, 11, 1, 11, 2, 11, 6, 11]

print(lista)
print(remover_repetidos(lista))
