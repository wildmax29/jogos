def jogar():


    print("***********************************")
    print("Bem vindo no jogo de forca!")
    print("***********************************")


    palavra_secreta = "banana".upper()
    letras_acertadas =["_","_","_","_","_","_"]
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra?")
        chute = chute.strip().upper()

        if(chute and palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index]=letra
                index = index + 1
        else:
            erros = erros +1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        if(acertou):
            print("Você Ganhou!!")

        else:
            print("Você perdeu!!")

    print("Fim de jogo")

    if(__name__ == "__main__"):
        jogar()