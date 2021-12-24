def jogar():
    print("********************************")
    print("Bem-vindo ao jogo de forca")
    print("********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = str(input("Qual letra? \n"))
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(chute,index))

            index+=1

        print("Jogando...")

    print("Fim do jogo")

if(__name__=="__main__"):
    jogar()
