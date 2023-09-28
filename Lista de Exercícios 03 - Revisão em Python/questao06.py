# 6. Escreva um programa que recebe uma string e conta a quantidade de vogais (a, e, i, o, u) presentes nela.

texto = input("Escreva qualquer texto: ")

contador = 0

for i in texto:
    if i in "aeiou" or i in "AEIOU":
        contador += 1

print(f'Frase: "{texto}"')
print(f"Quantidade de vogais: {contador}")
