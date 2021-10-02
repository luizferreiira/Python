#02) Crie uma matriz bidimensional com 4 linhas e 4 colunas e só insira valores como na figura abaixo:
##Sendo que somente na diagonal da matriz será preenchido um número.Apresente a soma desses números.


def soma():
  soma = 0
  for i in range(4):
    for j in range(4):
      if mat[i][j] > 0:
        soma+=mat[i][j]

  print(soma)


print('*PROGRAMA PRINCIPAL*')



mat = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(4):
  linha=[]
  for j in range(4):
    mat[i][j] = int(input('digite um número: '))

for i in range(4):
  print(mat[i])


print('RESULTADO DA SOMA')
soma()


