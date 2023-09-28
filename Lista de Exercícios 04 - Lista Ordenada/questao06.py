# Escreva um programa que ordene um vetor de inteiros em ordem decrescente e, em seguida,
# conte quantos números pares e quantos números ímpares existem no vetor ordenado.

def ordenar_dec(lista):
    for i in range(len(lista)):
        indice_minimo = i
        for j in range(i + 1, len(lista)):
            if lista[j] > lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]


def contar_par_impar(lista):
    contador_pares = 0
    contador_impares = 0
    for i in lista:
        if i % 2 == 0:
            contador_pares += 1
        else:
            contador_impares += 1
    return f"Quantidade de pares: {contador_pares}\nQuantidade de ímpares: {contador_impares}"


lista = [11, 3, 8, 9, 1, 7, 12, 2, 5, 13, 6, 10, 4]

# ordenar_dec(lista)

print(contar_par_impar(lista))
