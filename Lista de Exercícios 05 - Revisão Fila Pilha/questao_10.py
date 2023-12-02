# 10. Palíndromos são palavras, frases ou sequências que mantêm sua mesma forma quando invertidos.
# Por exemplo, a palavra "radar" é um palíndromo, pois se você a ler de trás para frente,
# ela ainda será "radar". Construa um programa que possa ler uma palavras ou frase e dizer
# se ela é um Palíndromo, use a estrutura de pilha para responder essa questão.

# Importe a classe Pilha
from pilha import Pilha

def e_palindromo(texto):
    # Remove espaços e converte para minúsculas
    texto = texto.replace(" ", "").lower()

    # Inicializa uma pilha
    pilha = Pilha()

    # Adiciona cada caractere do texto à pilha
    for caractere in texto:
        pilha.empilhar(caractere)

    # Compara os caracteres com a segunda metade do texto
    for caractere in texto:
        if pilha.desempilhar() != caractere:
            return False

    return True

# Exemplo de uso
texto = input("Digite uma palavra ou frase: ")
if e_palindromo(texto):
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
