arquivo = open("//home//luiz//Documentos//arqcomVetor.txt", "r+")

def criaArquivo():
  arquivo = open("c:\\Temp\\arqTeste.txt", "a")
  arquivo.write(str("Linha01\n"))
  arquivo.write(str("Linha02\n"))
  arquivo.write(str("Linha03\n"))

  print("Arquivo criado")
  arquivo.close()



def criaArquivoComVetor():
  arquivo = open("//home//luiz//Documentos//arqcomVetor.txt", "a")
  arquivo.writelines((["Linha01\n" ,"Linha02\n", "Linha03\n"]))
  print('arquivo criado')
  arquivo.close()



def criaArquivoAlteraLinhas():
  arquivo = open("//home//luiz//Documentos//arqcomVetor.txt", "r+")
  arquivo.seek(8)
  arquivo.write(str(chr(9) +"LinhaNova\n"))
  arquivo.close()

  print('Arquivo alterado a partir do byte 8')


def carregaArquivo():
  arquivo.seek(10)
  print('Leitura a partir do byte 10: %s' % arquivo.tell())
  print(arquivo.read(5))



def carregaArquivoAteoFim():
  lista=[]
  print('Lendo várias linhas e armazenando numa lista')
  for linha in arquivo:
    lista.append(linha)
  arquivo.close()
  print('Exibe linha 2: %s' % lista[1])
  print('Exibe linha 3: %s' % lista[2])

  



##carregaArquivo()
##criaArquivo()
##criaArquivoComVetor()
##criaArquivoAlteraLinhas()
carregaArquivoAteoFim()


  
