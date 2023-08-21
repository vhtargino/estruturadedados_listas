# 2. Crie um programa que determine se um número inserido pelo usuário é par ou ímpar.

num = float(input("Digite um número: "))

if num % 2 == 0:
    print(f"{num} é par.")
else:
    print(f"{num} é ímpar.")