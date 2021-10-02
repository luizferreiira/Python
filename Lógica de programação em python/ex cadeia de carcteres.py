#Instruções
#Informe uma frase qualquer:
#Eu amo a tia Eva

#01)Exibir a qtd de caracteres;
#02)Exibir a qtd de vogais;
#03)Exibir a qtd de palavras;
#04)Converter todas as letras para minúsculas;
#05)Cifrar todas vogais somando mais 4 posições e subtrair 6 posições nos outros caracteres;  --- entendi o conceito mas nao consegui implementar nesse código
#06)Exibir a frase normal e a frase cifrada --- frase normal ja está impressa

def funcaoCifrar():
  letrasAsc01 = ord(lista[0])+4
  letrasAsc02 = ord(lista[1])+4
  variavelcifrada = ""+chr(letrasAsc01)+chr(letrasAsc02)
  print('A variavel cifrada é: %s'%variavelcifrada)

  
lista = ["Eu amo Jesus"]
palavra = ['Eu','amo','Jesus']

qtd = 0
qtd2 = 0
cont1 = 0
cont2= 0
for i in lista:
  print(lista)
  
  for j in i:
    if j.lower() in "aeiou":
      qtd+=1
      
    if j in i:
      qtd2+=1


print('A palavra de {} caracteres.'.format(qtd2))
print("A palavra tem {} vogais.".format(qtd))
print('A frase contém {} palavras.'.format(len(palavra)))
print('A frase em letras minúsculas ficará assim: "{}"'.format(i.lower()))







