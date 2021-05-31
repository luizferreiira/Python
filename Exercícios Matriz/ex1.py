#1. Escreva um programa que leia uma matriz de ordem 3 x 5 de elementos inteiros,
#calcule e mostre na tela:
#a) menor número da matriz;
#b) soma dos números múltiplos de 3 da matriz;
#c) maior número da 3ª coluna da matriz (índice 2);
#d) média dos números da matriz;

from random import randint

mat=[]

for i in range(3):
    linha=[]
    for j in range(5):
        linha.append(randint(1,10))

    mat.append(linha)

for i in range(3):
    print(mat[i])


menor = mat[0][0]
soma=tot=0
maior = mat[0][2]
for i in range(3):
    for j in range(5):
        if mat[i][j] < menor:
            menor = mat[i][j]
            
        if mat[i][j] % 3 == 0:
            soma+=mat[i][j]
            
        if mat[i][2] > maior:
            maior = mat[i][2]

        tot+=mat[i][j]

media = tot/15

print('menor número da matriz: ',menor)
print('soma dos números múltiplos de 3 da matriz: ',soma)
print('maior número da 3ª coluna da matriz: ',maior)
print('média dos números da matriz: ',media)


