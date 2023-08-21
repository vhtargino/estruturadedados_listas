# 5. Faça um programa que leia uma lista de números e retorne a média dos números pares.

numeros = [3, 66, 987, 12, 1, 45, 332, 70]
numeros_pares = []

for i in numeros:
    if i % 2 == 0:
        numeros_pares.append(i)

media_pares = sum(numeros_pares) / len(numeros_pares)

print(media_pares)
