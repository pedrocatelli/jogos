import forca

def escolher_jogo():
    print("**************************")
    print("Escolha seu jogo")
    print("**************************")

    print("(1) Forca (2) Advinhação")

    escolha = int(input("Qual jogo? "))

    if escolha == 1:
        forca.jogar()

if (__name__ == "__main__"):
    escolher_jogo()