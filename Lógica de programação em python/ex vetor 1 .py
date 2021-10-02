
def vet(vt01,vt02):
  vtmultiplica = []
  for i in range(3):
    multiplica = vt01[i] * vt02[i]
    vtmultiplica.append(multiplica)

  print(vtmultiplica)


vt01 = []
vt02 = []
for i in range(3):
  print('Digite um número: ')
  vt01.append(int(input()))
for i in range(3):
  print('Digite outro número: ')
  vt02.append(int(input()))
  
print(vt01,vt02)
vet(vt01,vt02)

            
  
