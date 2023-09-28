# 8. Escreva um programa que converte uma temperatura em Celsius para Fahrenheit ou vice-versa, dependendo da escolha do usuário.

def celsius_para_farenheit(graus_celsius):
    conversao_para_farenheit = graus_celsius * 1.8 + 32
    return conversao_para_farenheit


def farenheit_para_celsius(graus_farenheit):
    conversao_para_celsius = 5* ((graus_farenheit - 32)/9)
    return conversao_para_celsius


escolha = ""

while escolha not in ["1", "2"]:
    print("Escolha:")
    print("1. Converter de Celsius para Farenheit")
    print("2. Converter de Farenheit para Celius")
    escolha = input("Digite sua escolha: ")

if escolha == 1:
    graus_celsius = float(input("Qual a temperatura em Celsius? Digite apenas números: "))
    print(f"{graus_celsius:.1f}°C é o mesmo que {celsius_para_farenheit(graus_celsius):.1f}°F")
else:
    graus_farenheit = float(input("Qual a temperatura em Farenheit? Digite apenas números: "))
    print(f"{graus_farenheit:.1f}°F é o mesmo que {farenheit_para_celsius(graus_farenheit):.1f}°C")
