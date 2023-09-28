# 4. Escreva um programa que recebe um número inteiro positivo e calcula a soma de seus dígitos.

num = int(input("Digite um número inteiro positivo: "))
num_convertido = str(num)
soma = 0

for i in num_convertido:
    novo_num = int(i)
    soma += novo_num

print(soma)
