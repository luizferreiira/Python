
##Crie um algoritmo para inserir 3 códigos de produtos, 3 nomes de produtos e valores de produtos.
#Depois exiba esses valores inseridos nas matrizes como na tabela abaixo:

##Depois peça para o usuário digitar um código de produto e se ele existir peça para ele inserir
#a  quantidade  e  exiba  o  valor  total  da  compra  assim  como  o  nome  do  produto escolhido.


vetcod = []
vetprod=[]
vetvalor=[]
def inserir():
  for i in range(3):
    print('informe o código do produto: ')
    vetcod.append(int(input()))
    print('informe o nome do produto: ')
    vetprod.append(str(input()))
    print('informe o valor do produto: ')
    vetvalor.append(float(input()))


def exibir():
  for i in range(3):
    print('código do produto na posição %i'%i, vetcod[i])
    print('nome do produto na posição %i'%i, vetprod[i])
    print('valor do produto na posição %i'%i, vetvalor[i])


def vender():
  print('Querido usuário, digite um código: ')
  codigo=int(input())
  for i in range(3):
    if (codigo == vetcod[i]):
      print('informe a quantidade de produtos')
      qtd = floa(input())
      total = qtd * vetvalor[i]
      print('O total da compra foi: %.2f'%total)
      print('O produto comprado foi: %s'%vetprod[i])
  

inserir()
exibir()
vender()









