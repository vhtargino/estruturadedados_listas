# 8. Em um programa de edição de texto, implemente a funcionalidade de 
# "Desfazer" e "Refazer" usando uma pilha para armazenar o histórico
# de comandos executados pelo usuário.

from pilha import Pilha

class EditorDeTexto:
    def __init__(self):
        self.texto = ""
        self.historico_comandos = Pilha()
        self.historico_desfazer = Pilha()

    def adicionar_texto(self, novo_texto):
        # Adiciona texto ao histórico de comandos
        self.historico_comandos.empilhar(self.texto)
        
        # Atualiza o texto
        self.texto += novo_texto
        print(f"Texto atual: {self.texto}")

    def desfazer(self):
        if not self.historico_comandos.is_vazia():
            # Desempilha o último estado
            estado_anterior = self.historico_comandos.desempilhar()
            # Adiciona o estado atual ao histórico de refazer
            self.historico_desfazer.empilhar(self.texto)
            # Atualiza o texto
            self.texto = estado_anterior
            print(f"Desfazer. Texto atual: {self.texto}")
        else:
            print("Não há ações para desfazer.")

    def refazer(self):
        if not self.historico_desfazer.is_vazia():
            # Desempilha o último estado
            estado_futuro = self.historico_desfazer.desempilhar()
            # Adiciona o estado atual ao histórico de comandos
            self.historico_comandos.empilhar(self.texto)
            # Atualiza o texto
            self.texto = estado_futuro
            print(f"Refazer. Texto atual: {self.texto}")
        else:
            print("Não há ações para refazer.")

# Exemplo de uso
editor = EditorDeTexto()

editor.adicionar_texto("Olá, ")
editor.adicionar_texto("mundo!")

editor.desfazer()

editor.refazer()