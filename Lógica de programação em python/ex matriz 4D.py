mlinha=[] #Vetor sem tamanho definido
for linha in range(0,2): #qual será o limite da leitura
    mcoluna=[] #Dentro de cada linha sera inserida uma coluna
    for coluna in range(0,2):
          mprofundidade=[]
          for profundidade in range(0,2):
               m4d=[]
               for quartadim in range(0,2):
                   m4d.insert(quartadim,str(input())) #insira no vetor, no indice um valor string
               mprofundidade.insert(profundidade,m4d)
          mcoluna.insert(coluna,mprofundidade)
    mlinha.insert(linha,mcoluna)  


for linha in range(0,2): #Será o limite da leitura
    for coluna in range(0,2):
      for profundidade in range(0,2):
          for quartadim in range(0,2):
             print("linha", linha, "coluna", coluna, "profundidade", profundidade, "4d", quartadim)
             print(mlinha[linha][coluna][profundidade][quartadim])
             print(end=" ")
             
elementos=[]
for linha in range(0,2):
    for coluna in range(0,2):
        for profundidade in range(0,2):
            for quartadim in range(0,2):
                elementos.append(mlinha[linha][coluna][profundidade][quartadim])

print(elementos)
    
