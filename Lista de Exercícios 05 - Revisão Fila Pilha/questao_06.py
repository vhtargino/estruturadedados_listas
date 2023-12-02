# 6. Imagine que você está desenvolvendo um navegador web simplificado.
# Use uma pilha para armazenar o histórico de páginas visitadas pelos usuários
# e implementar as funcionalidades de voltar e avançar na navegação.

from pilha import Pilha

class NavegadorWeb:
    def __init__(self):
        self.historico = Pilha()
        self.futuro = Pilha()

    def abrir_pagina(self, pagina):
        print(f"Abrindo a página: {pagina}")
        self.historico.empilhar(pagina)
        # Ao abrir uma nova página, o histórico futuro é limpo
        self.futuro = Pilha()

    def voltar_pagina(self):
        if not self.historico.is_vazia():
            pagina_atual = self.historico.desempilhar()
            print(f"Voltando para a página anterior: {pagina_atual}")
            self.futuro.empilhar(pagina_atual)

    def avancar_pagina(self):
        if not self.futuro.is_vazia():
            pagina_futura = self.futuro.desempilhar()
            print(f"Avançando para a próxima página: {pagina_futura}")
            self.historico.empilhar(pagina_futura)

    def visualizar_historico(self):
        print("Histórico de páginas visitadas:")
        self.historico.imprimir()

# Exemplo de uso
navegador = NavegadorWeb()

navegador.abrir_pagina("www.exemplo.com")
navegador.abrir_pagina("www.exemplo2.com")
navegador.abrir_pagina("www.exemplo3.com")

navegador.voltar_pagina()
navegador.avancar_pagina()

navegador.visualizar_historico()
