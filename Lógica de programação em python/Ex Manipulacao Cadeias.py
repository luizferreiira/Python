print("Informe um nome")
nome = str(input())

def funcoesSimples():
     print("O nome é: %s"%nome)
     tamanho = len(nome) ###Fatec IIES
     print("A qtd de letras é %i"%tamanho)
     substituiLetras=nome.replace("B","A") ##BIA -->AIA
     print("A string ficou %s"%substituiLetras)
     substituiNome=nome.replace("BIA","MARIA")
     print("A string ficou %s"%substituiNome)
     retornaPosicao=nome.find("BI")
     print("A posição que se encontra a letra B é %i"%retornaPosicao)
     sobrenome=" VITÓRIA"
     nomeConcatenadoApartirdoEspaco = nome.join(sobrenome.split(" "))
     #se repetir os espaços ele vai repetir a junção
     print("Nome concatenado é: %s"%nomeConcatenadoApartirdoEspaco)
     nomeConcatenado = nome + sobrenome
     print("Nome concatenado simplee é: %s"%nomeConcatenado)
     nomeMinusculo=nome.lower()
     nomeMaiusculo=nome.upper()
     nomeInverteLetras="FATEC iies"
     nomeInverteLetras=nomeInverteLetras.swapcase()
     print("Minúsculo %s"%nomeMinusculo)
     print("Maiúsculo %s"%nomeMaiusculo)
     print("Nome com caracteres invertidos %s"%nomeInverteLetras)
     stringApartirdaPosicao=nome[0:2] ###BIA
     print("Copia somente as duas primeiras letras: %s"%stringApartirdaPosicao)
     nomeGrande="    JOSE MARIA NUNES CAMARGO    "
     print("Nome com espaços %s"%nomeGrande)
     tiraLetras=nomeGrande.strip()
     print("Retira os espaços %s"%tiraLetras)
     print("Imprime somente os cinco primeiros caracteres %.5s"%nomeGrande)

     
     if nome.isalpha():
          print("Contém números ou letras")
     if nome.isdigit():
          print("A variável nome é númérica")

     conta=int(0)

     for indice in range (0,len(nome)): ##BEATRIZ *CHAR
         if(ord(nome[indice])>=65 and ord(nome[indice])<=90):
               conta=conta+1
     
     if conta==int((len(nome))):
          print("Somente letras maiúsculas")
     
def funcoesParaComparar():
     var01="ABC"
     var02="CDE"
     if var01==var02:
          print("As strings são iguais")
     else:
          print("As strings são diferentes")      
                
     if "A" in var01:
          print("A letra A está na variável var01")
     else:
          print("A letra A não está na cadeia")      


     if var01>var02:
          print("A variável 01 é maior que a variável 02")
     elif var01<var02:
          print("A variável 01 é menor que a variável 02")      
     else:
          print("A variável 01 é igual a variável 02")


def funcaoCifrar():
     letraAsc01 = ord(nome[0])+3 #Pegou a primeira letra e retorno do ASC 
     letraAsc02 = ord(nome[1])+3 #Pegou a segunda letra e retorno do ASC    
     letraAsc03 = ord(nome[2])+3 #Pegou a terceira letra e retorno do ASC
     variavelCifrada=""+chr(letraAsc01)+chr(letraAsc02)+chr(letraAsc03) 
     print("A variavel cifrada é: %s"%variavelCifrada)

##funcoesSimples()
funcoesParaComparar()
##funcaoCifrar()     

