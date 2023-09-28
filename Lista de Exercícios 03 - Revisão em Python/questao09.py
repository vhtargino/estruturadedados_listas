# 9. Crie uma calculadora que realiza operações de adição, subtração, multiplicação e divisão, com base na escolha do usuário.

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        print("Não é possível dividir por zero.")
    else:
        return a / b


num1 = float(input("Digite o primeiro número: "))

escolha = ""

while escolha not in ["1", "2", "3", "4"]:
    print("Escolha a operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    escolha = input("Digite sua escolha: ")

num2 = float(input("Digite o segundo número: "))

if escolha == "1":
    print(f"{num1} + {num2} = {somar(num1, num2)}")
elif escolha == "2":
    print(f"{num1} - {num2} = {subtrair(num1, num2)}")
elif escolha == "3":
    print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
else:
    if num2 == 0:
        print("Não é possível dividir por zero.")
    else:
        print(f"{num1} / {num2} = {dividir(num1, num2)}")
