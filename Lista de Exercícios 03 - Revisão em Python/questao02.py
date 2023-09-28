# 2. Escreva uma função que calcula o fatorial de um número inteiro positivo fornecido pelo usuário.

num = int(input("Digite um número inteiro positivo: "))

contador = num
fatorial = 1

while contador > 0:
    fatorial *= contador
    contador -= 1

print(fatorial)
