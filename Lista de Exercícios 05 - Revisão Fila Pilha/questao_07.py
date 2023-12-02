# 7. Crie uma calculadora que avalia expressões matemáticas no formato Notação Polonesa Reversa (RPN).
# Use uma pilha para armazenar os operandos e operadores e realizar os cálculos.

from pilha import Pilha

def calculadora_rpn(expressao):
    pilha = Pilha()

    # Função auxiliar para verificar se um token é um operador
    def eh_operador(token):
        return token in {'+', '-', '*', '/'}

    # Divida a expressão em tokens
    tokens = expressao.split()

    for token in tokens:
        if token.isnumeric() or (token[0] == '-' and token[1:].isnumeric()):
            # Se o token for um número (positivo ou negativo), empilhe na pilha
            pilha.empilhar(float(token))
        elif eh_operador(token):
            # Se o token for um operador, desempilhe dois operandos, aplique o operador e empilhe o resultado
            if pilha.tamanho() < 2:
                print("Erro: Expressão inválida. Não há operandos suficientes para o operador.")
                return None
            else:
                operando2 = pilha.desempilhar()
                operando1 = pilha.desempilhar()
                resultado = realizar_operacao(operando1, operando2, token)
                pilha.empilhar(resultado)
        else:
            print(f"Erro: Token desconhecido encontrado: {token}")
            return None

    # No final, o resultado deve ser o único item na pilha
    if pilha.tamanho() == 1:
        return pilha.desempilhar()
    else:
        print("Erro: Expressão inválida. Número incorreto de operandos e operadores.")
        return None

def realizar_operacao(operando1, operando2, operador):
    if operador == '+':
        return operando1 + operando2
    elif operador == '-':
        return operando1 - operando2
    elif operador == '*':
        return operando1 * operando2
    elif operador == '/':
        if operando2 == 0:
            print("Erro: Divisão por zero.")
            return None
        else:
            return operando1 / operando2

# Exemplo de uso
expressao_rpn = "3 4 + 2 *"
resultado = calculadora_rpn(expressao_rpn)

if resultado is not None:
    print(f"Resultado da expressão RPN: {resultado}")
