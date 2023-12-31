# Escreva uma função em Python para ordenar um vetor de inteiros, ele deve receber um parâmetro
# que serve como chave para realizar a ordenação crescente ou decrescente.

def ordenar(lista, bool):
    if bool == False: # Ordem crescente
        for i in range(len(lista)):
            indice_minimo = i
            for j in range(i + 1, len(lista)):
                if lista[j] < lista[indice_minimo]:
                    indice_minimo = j
            lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    else: # Ordem decrescente
        for i in range(len(lista)):
            indice_minimo = i
            for j in range(i + 1, len(lista)):
                if lista[j] > lista[indice_minimo]:
                    indice_minimo = j
            lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]


lista = [11, 3, 8, 9, 1, 7, 12, 2, 5, 13, 6, 10, 4]

print(lista)
# ordenar(lista, True)
ordenar(lista, False)
print(lista)
