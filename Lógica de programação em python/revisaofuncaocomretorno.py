#Revisão função com retorno

def fquad(num):
    percorre=0
    total=0
    while (percorre < 3):
        total +=num**2
        percorre +=1
    return total

total = fquad(5)
print(total)
