print("**************************")
print("Bem-vindo ao Jogo da Forca")
print("**************************")

print("Fim de Jogo.")

def jogar():
    print("Jogando Forca")
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    palavra_chave = "girafa"

    print(letras_acertadas)
    print(letras_acertadas)
    acertou = False
    enforcou = False

    count = 0
    while(not enforcou and not enforcou):
        chute = input("Qual a letra? ")
        chute = chute.strip()

        index = 0


        for letra in palavra_chave:
            if letra.upper() == chute.upper():
                print(f"Encontrei a letra {chute} na posição {index}")
                letras_acertadas[index] = chute
                print(letras_acertadas)
                count += 1
                print(count)
                print(len(palavra_chave))
            index += 1

        if count == len(palavra_chave):
            break

    print("Fim do Jogo")

if (__name__ == "__main__"):
    jogar()