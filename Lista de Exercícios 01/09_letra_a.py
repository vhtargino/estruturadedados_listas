# 9. Escreva um programa que leia uma lista de nomes e retorne uma nova lista com apenas os nomes que começam com a letra 'A'.

nomes = ["amélia", "joão", "barnabé", "amaro", "paulo", "marcos", "nelson", "antônio", "amanda", "ricardo", "ulisses", "abel"]
nomes_com_a = []

for i in nomes:
    if i[0] == "a":
        nomes_com_a.append(i)

print(nomes_com_a)
