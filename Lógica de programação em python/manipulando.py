arquivo = open("//home//luiz//Documentos//media.txt", "r")

def lerArquivo():
  print(arquivo.read())
  arquivo.close()


def carregaArquivo():
  resp='S'
  while (resp=='S' or resp=='s'):
    arquivo.seek(5)
    print('Informe a nota da p1: ')
    p1 = float(arquivo.read(2))
    arquivo.seek(18)
    print('Informe a nota do projeto:')
    p2=float(arquivo.read(1))
    arquivo.seek(29)
    print('Informe a pontuação das listas:')
    p=float(arquivo.read(1))
    

    media = p1 * 0.3 + ((p2*40)/100) + p

    if media >= 6:
        print('Aprovado com média: %i'%media)
    elif media <6:
        print('informe a nota da p1 sub:')
        sub=int(input())
        if media >=6:
            print('Aprovado com média: %i'%media)
        else:
            print('Reprovado com média: %i'%media)

    print('Deseja repetir a operação? ')
    resp=input()


carregaArquivo()




#lerArquivo()
