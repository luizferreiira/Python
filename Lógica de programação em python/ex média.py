#calculo da média da disciplina
#inserir a nota da p1 (30%)
#inserir a nota do projeto (40%)
#inserir a pontuação das listas (até 5 pontos)
#exibir se o aluno está aprovado e com média .... média.
#pedir para inserir novamente a nota da p1 (seria a sub)
#recalcular média
#exibir situação se está aprovado ou reprovado na disciplina
resp='S'
while (resp=='S' or resp=='s'):
    
    print('Informe a nota da p1: ')
    p1=int(input())
    print('Informe a nota do projeto: ')
    p2=int(input())
    print('Informe a pontuação das listas: ')
    p=int(input())

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

