# 3. Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”.
# Implemente um método chamado “calcular_area” que retorna a área do retângulo.

class Retangulo:
    def __init__ (self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        area = self.base * self.altura
        return area


ret = Retangulo(5, 6)

print(ret.calcular_area())
