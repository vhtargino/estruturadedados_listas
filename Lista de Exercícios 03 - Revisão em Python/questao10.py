# 10. Escreva uma função que gera a sequência de Fibonacci até um determinado número de termos especificado pelo usuário.

num = int(input("Digite um número: "))

lista_fib = [0, 1]

while lista_fib[-1] + lista_fib[-2] <= num:
    proximo_fib = lista_fib[-1] + lista_fib[-2]
    lista_fib.append(proximo_fib)

for i in lista_fib:
    print(i)
