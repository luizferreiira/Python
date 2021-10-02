
vt01 = [10,20,30]
vt02 = [2,4,6]
vtmult=[]
vtmultinvertida=[]

def vet():
  print('Exibe multiplicação')
  for i in range(3):
    vtmult.append(vt01[i] * vt02[i])
    print("No indice %i"%i, "ficou o valor %i"%vtmult[i])

def fmultinvertida():
  print('Exibe multiplicação invertida')
  for i in range(3):
    vtmultinvertida.append(vt01[i]*vt02[2-i])
    print("No indice %i"%i, "ficou o valor %i"%vtmultinvertida[i])

fmultinvertida()
vet()
