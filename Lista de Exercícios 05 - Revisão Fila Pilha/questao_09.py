# 9. Crie uma estrutura que possa ler uma expressão matemática do tipo (2+3)*(8-9)/(7^3)
# e apresente todos os operadores matemáticos existente nessa expressão,
# utilize a pilha para responder a questão.

from pilha import Pilha

def obter_operadores(expressao):
    pilha = Pilha()
    operadores = []

    for caractere in expressao:
        if caractere in {'+', '-', '*', '/', '^', '(', ')'}:
            pilha.empilhar(caractere)
            operadores.append(caractere)

    return operadores

# Exemplo de uso
expressao_matematica = "(2+3)*(8-9)/(7^3)"
operadores = obter_operadores(expressao_matematica)

print("Operadores matemáticos na expressão:")
for i in operadores:
    print(i)
