# 5. Crie uma função que verifica se um número é primo ou não.

num = int(input("Digite um número: "))

if num == 1:
    print(f"{num} não é primo.")
elif num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(f"{num} não é primo.")
            break
    else:
        print(f"{num} é primo.")
else:
    print(f"{num} não é primo.")
