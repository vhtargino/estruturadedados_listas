# 9. Crie uma classe chamada “Triangulo” com atributos “lado1”, “lado2” e “lado3”.
# Implemente um método chamado “calcular_perimetro” que retorna o perímetro do triângulo.

class Triangulo:
    def __init__ (self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_perimetro(self):
        perimetro = self.lado1 + self.lado2 + self.lado3
        return f"O perímetro do triângulo é {perimetro}."


triang1 = Triangulo(5, 7, 8)

print(triang1.calcular_perimetro())
