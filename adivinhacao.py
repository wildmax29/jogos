import random


print("Bem vindo no jogo de advinhação!")
print("***********************************")

numero_secreto =random.randrange(1,101) #random gera um número entre 0.0 1.0
total_de_tentativas = 3
rodada =1

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
        print("Você acertou")
        break
    else:
        if (maior):
            print("Você errou!! tente novamente informando um número maior")
        elif(menor):
            print("Você errou!! Tente novamente informando um número menor")


    'rodada = rodada + 1'

print("Fim de jogo")