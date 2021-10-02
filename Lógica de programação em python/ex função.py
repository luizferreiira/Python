##exercício 1 revisão função

def fsoma(num):
    total = float(0)
    total=num + 20
    print('A soma do número %.2f'%num, " mais 20 é: %.2f"%total)
    return total

def fmult(num):
    total = float(0)
    total=num * 3
    print('A mult do número %.2f'%num, " por 3 é: %.2f"%total)
    return total


print('Informe um número: \n')
numero = float(input())

##print(fsoma(numero))
resultadofunc = fsoma(numero)

##print(fmult(resultadofunc))
resultadofunc = fmult(resultadofunc)




