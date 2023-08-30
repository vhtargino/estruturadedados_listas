# 10. Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”.
# Implemente um método chamado “aumentar_salario” que recebe um valor percentual de aumento e atualiza o salário do funcionário.

class Funcionario:
    def __init__ (self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def aumentar_salario(self, percentual):
        self.salario = self.salario + (self.salario * (percentual/100))
        return self.salario


func1 = Funcionario("Seu Cebola", 5000, "Contador")
print(func1.salario)

func1.aumentar_salario(20)
print(func1.salario)
