#02)De acordo com o texto abaixo crie um algoritmo usando funções.
#O senhor Airton tem uma loja de roupas e calçados situada na cidade de Conchas,
#ele vende no atacado e varejo tendo situações diferentes para cada situação sendo que
#normalmente seu procedimento de vendas tem sido o seguinte:
#Na compra de calçados no varejo ele faz a seguinte verificação:
#Consulta o cliente
#-Se o cliente é devedor ele vende a mercadoria somente à vista
#-Se o cliente é adimplente (paga em dia) então ele oferece as seguintes
#condições:
#-Se o cliente vai comprar a vista
#-Se for a dinheiro então
#-Concede 20% de desconto
#-Se for em cheque então
#-Concede 15% de desconto
#-Se o cliente vai comprar a prazo ele oferece as seguintes condições:
#-Se comprar em duas vezes então
#-Conceder 5% de desconto
#-Se comprar em três vezes então
#-Não conceder desconto
#-Se comprar em quatro ou mais vezes então
#-5% de acréscimo no valor total da venda

def consul():
  if pagamento == "dinheiro" or pagamento =="DINHEIRO":
    print('O cliente tem direito a 20% de desconto!')
  elif pagamento == "cheque" or pagamento == "CHEQUE":
    print('O cliente tem direito a 15% de desconto!')

def praz():
  if qtd == "2x":
    print('O cliente tem direito a 5% de desconto!')
  elif qtd == "3x":
    print('O cliente não tem direito a desconto!')
  elif qtd == "5x+":
    print('-5% de acréscimo no valor total da venda')
    


print('Informe se é devedor ou adimplente:')
consulta = str(input())
while consulta != "sair":
  if consulta == "devedor" or consulta == "DEVEDOR":
    print('Pagamento somente a vista!')
  else:
    print('pagamento a vista em dinheiro,cheque ou a prazo? ')
    pagamento = str(input())
    if pagamento == "prazo" or pagamento == "PRAZO":
      print('informe em quantas vezes irá pagar: (2x - 3x - 5x+)')
      qtd = str(input())
      praz()
    consul()

  
  print('Informe se é devedor ou adimplente ou digite (SAIR):')
  consulta = str(input())




  

  
  
  



