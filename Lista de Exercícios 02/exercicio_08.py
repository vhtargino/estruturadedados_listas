# 8. Crie uma classe chamada “Aluno” com atributos “nome” e “notas”.
# Implemente um método chamado “calcular_media” que retorna a média das notas do aluno.

class Aluno:
    def __init__ (self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    
    def calcular_media(self):
        media = (self.nota1 + self.nota2)/2
        return f"A média de {self.nome} é {media}"

aluno1 = Aluno("Cascão", 7.6, 8.9)

print(aluno1.calcular_media())
