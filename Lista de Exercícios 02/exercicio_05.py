# 5. Crie uma classe chamada “Pessoa” com atributos “nome” e “idade”.
# Implemente um método chamado “falar” que imprime uma mensagem com o nome da pessoa.

class Pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


pessoa1 = Pessoa("Cebolinha", 7)

pessoa1.falar()
