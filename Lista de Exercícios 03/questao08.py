def encontrar_mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista)
    if n % 2 == 0:
        meio1 = lista_ordenada[n // 2- 1]
        meio2 = lista_ordenada[n // 2]
        return (meio1 + meio2) / 2
    else:
        return lista_ordenada[n // 2]


lista = [11, 3, 8, 9, 1, 7, 12, 2, 5, 13, 6, 10] # De 1 a 13, sem o número 4

print(sorted(lista))
print(encontrar_mediana(lista))
