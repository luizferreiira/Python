#ex fatorial

#def fatorialsemrecursividade(n):
  #fatorial = 1
  #for i in range(n, 0, -1):
    #fatorial = fatorial * i
    #print(fatorial)


#print('informe um número: ')
#n = int(input())
#fatorialsemrecursividade(n)


def fatorialcomrecursividade(n):
  if n == 0:
    return 1
  else:
    return n * fatorialcomrecursividade(n-1)



print('Informe um número: ')
num = int(input())
print(fatorialcomrecursividade(num))

    
    
    

  
    

