import random
def jogar():
    print("********************************")
    print("Bem-vindo ao jogo de adivinhação")
    print("********************************")

    numero_secreto = random.randint(1, 100)
    total_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Digite um nível: \n"))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}: ".format(rodada, total_tentativas))
        print("Digite um número entre 1 e 100: ")
        chute = int(input(""))
        print("Você digitou: ", chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = (numero_secreto == chute)
        maior = (chute > numero_secreto)
        menor = (chute < numero_secreto)

        if (acertou):
            print("Parabéns você acertou e fez {} pontos".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)  # 40-20
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if(__name__=="__main__"):
    jogar()
