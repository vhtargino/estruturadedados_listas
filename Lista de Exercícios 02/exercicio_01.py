# 1. Crie uma classe chamada “Circulo” que tenha um atributo “raio”.
# Implemente um método chamado “calcular_area” que retorna a área do círculo.

class Circulo:
    def __init__ (self, raio):
        self.raio = raio
    
    def calcular_area(self):
        area = 3.14 * (self.raio ** 2)
        return area


c1 = Circulo(5)

print(c1.calcular_area())
