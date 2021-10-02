def vet():
  vt01 = [10,20,30]
  vt02 = [2,4,6]
  vtmult=[]
  for i in range(3):
    vt01.reverse()
    vt02.reverse()
    vtmult.append(vt01[i] * vt02[i])

  print(vt01,vt02)
  print(vtmult)

vet()
