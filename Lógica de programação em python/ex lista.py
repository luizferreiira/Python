##01) Crie um algoritmo onde o usuário possa escolher uma unidade
#de medida distancias,
#capacidade (litros), peso e bytes. Depois peça para ele digitar
#um valor qualquer e
#aparecer na tela como no exemplo:
#1 km equivale a:
#• 0.625 Milhas
#• 1000 Metros
#• 100000 Centímetros
#• 1000000 Milímetros
#Ao final perguntar se ele deseja exibir novamente.
#Colocar cada opção em uma função

def escolher(num):
    if escolha == "capacidade":
        l = numero * 1000
        l2 = l * 1000
        l3 = l2 * 1000
        l4 = l3 * 1000
        print("%.2f"%num,"metros cúbicos equivalem a: ")
        print("%.2f"%l, "litros")
        print("%.2f"%l2, "mililitros")
        print("%.2f"%l3, "centilitros")
        print("%.2f"%l4, "decilitros")
        return (l,l2,l3,l4)

def pesar(num):
    if escolha == "peso":
        g = numero * 1000 
        g2 = g * 1000
        print("%.2f"%num, "litros equivalem a: ")
        print("%.2f"%g, "gramas")
        print("%.2f"%g2, "miligramas")
        return (g,g2)

def tamanho(num):
  if escolha == "bytes":
    mb = numero * 1000
    kb = mb * 1000
    b = kb * 1000
    print("%.2f"%num,"Gigabytes equivalem a: ")
    print("%.2f"%mb, "Megabytes")
    print("%.2f"%kb, "Kilobytes")
    print("%.2f"%b, "Bytes")
    return (mb,kb,b)




resp = "S"
while (resp == "S" or resp == "s"):
  print('Escolha uma unidade medida: (capacidade - peso - bytes)')
  escolha = str(input())
  print('Informe um número: \n')
  numero = float(input())

  resultado = escolher(numero)
  resultado2 = pesar(numero)
  resultado3 = tamanho(numero)

  print('Deseja continuar escolhendo? (S/N)')
  resp = input()







