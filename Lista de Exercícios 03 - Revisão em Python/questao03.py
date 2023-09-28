# 3. Crie uma função que verifica se uma palavra ou frase é um palíndromo
# (lê-se igual de trás para frente, desconsiderando espaços e pontuação).

def palindromos(palavra):
    palavra_invertida = palavra[::-1]
    if palavra == palavra_invertida:
        print("A palavra é um palíndromo.")
    else:
        print("A palavra não é um palíndromo.")

palindromos("omissíssimo")
