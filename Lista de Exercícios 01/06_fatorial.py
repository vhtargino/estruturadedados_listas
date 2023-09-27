# 6. Escreva um programa que peça um número inteiro positivo ao usuário e calcule o fatorial desse número.

num = int(input("Digite um número inteiro positivo: "))

contador = num
fatorial = 1

while contador > 0:
    fatorial *= contador
    contador -= 1

print(fatorial)
