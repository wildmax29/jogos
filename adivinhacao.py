import random

def jogar():

    print("Bem vindo no jogo de advinhação!")
    print("***********************************")

    numero_secreto =random.randrange(1,101) #random gera um número entre 0.0 1.0
    total_de_tentativas = 3
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel==2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    print("numero {}".format(numero_secreto))

    'while(rodada <= total_de_tentativas):'
    for rodada in range(1,total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str= input("digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute < numero_secreto
        menor = chute > numero_secreto


        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))

            break
        else:
            if (maior):
                print("Você errou!! tente novamente informando um número maior")
                pontos_perdidos = abs(numero_secreto - chute) #calculo para perda de pontos
                pontos = pontos - pontos_perdidos
            elif(menor):

                print("Você errou!! Tente novamente informando um número menor")
                pontos_perdidos = abs(numero_secreto - chute) #calculo para perda de pontos
                pontos = pontos - pontos_perdidos

        'rodada = rodada + 1'

    print("Fim de jogo")
if(__name__=="__main__"):
    jogar()