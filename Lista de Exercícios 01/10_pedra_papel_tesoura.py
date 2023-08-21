'''10. Crie um programa que simule o jogo "Pedra, Papel e Tesoura" entre o usuário e o computador.
O programa deve solicitar a escolha do usuário e, em seguida, escolher aleatoriamente a escolha
do computador e determinar o vencedor.'''

import random

print("Bem vindo ao jogo de Pedra, Papel e Tesoura!")
opcoes = ["pedra", "papel", "tesoura"]

while True:

    while True:
        tentativa = input("\nEscolha pedra, papel ou tesoura: ").lower()
        if tentativa not in opcoes:
            print("\033[0;31mInválido!\033[0;0m")
            continue
        else:
            break

    escolha_computador = random.choice(opcoes)

    print(f"O computador escolheu \033[0;33m{escolha_computador}\033[0;0m!")

    if tentativa == escolha_computador:
        print("\033[0;34mEmpate!\033[0;0m\n")
    elif tentativa == opcoes[0] and escolha_computador == opcoes[1]:
        print("Papel derrota pedra! \033[0;31mVitória do computador!\033[0;0m\n")
    elif tentativa == opcoes[0] and escolha_computador == opcoes[2]:
        print("Pedra derrota tesoura! \033[0;32mVocê venceu!\033[0;0m\n")
    elif tentativa == opcoes[1] and escolha_computador == opcoes[2]:
        print("Tesoura derrota papel! \033[0;31mVitória do computador!\033[0;0m\n")
    elif tentativa == opcoes[1] and escolha_computador == opcoes[0]:
        print("Papel derrota pedra! \033[0;32mVocê venceu!\033[0;0m\n")
    elif tentativa == opcoes[2] and escolha_computador == opcoes[0]:
        print("Pedra derrota tesoura! \033[0;31mVitória do computador!\033[0;0m\n")
    elif tentativa == opcoes[2] and escolha_computador == opcoes[1]:
        print("Tesoura derrota papel! \033[0;32mVocê venceu!\033[0;0m\n")
    
    jogar_novamente = input("Deseja jogar novamente? [\033[0;32mS\033[0;0m/\033[0;31mN\033[0;0m]: ").lower()

    while jogar_novamente not in "sn":
        print("\033[0;31mInválido!\033[0;0m Escolha S (Sim) ou N (Não)!\n")
        jogar_novamente = input("Deseja jogar novamente? [\033[0;32mS\033[0;0m/\033[0;31mN\033[0;0m]: ").lower()
        
    if jogar_novamente == "s":
        continue
    elif jogar_novamente == "n":
        break

print("\n\033[0;31mGame over!\033[0;0m Obrigado por jogar!")
