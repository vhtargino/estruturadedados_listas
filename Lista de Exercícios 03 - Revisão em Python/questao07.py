# 7. Crie uma função que calcula o índice de massa corporal (IMC) de uma pessoa com base em sua altura e peso.

def imc(altura, peso):
    imc = peso / (altura**2)
    return imc


altura = float(input("Digite sua altura em metros (ex: 1.80): "))
peso = float(input("Digite seu peso em kg (ex: 93): "))

print(f"Seu IMC é {imc(altura, peso):.2f}.")
