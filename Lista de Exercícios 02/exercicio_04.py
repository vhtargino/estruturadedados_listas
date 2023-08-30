# 4. Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”.
# Implemente métodos “depositar” e “sacar” para manipular o saldo.

class ContaBancaria:
    def __init__ (self, saldo, titular):
        self.saldo = saldo
        self.titular = titular
    
    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo


conta1 = ContaBancaria(500, "João")

print(conta1.saldo, conta1.titular)

conta1.depositar(1000)
print(conta1.saldo)

conta1.sacar(400)
print(conta1.saldo)
