

valor = int(input("Digite o valor: "))

for num in range(1,25):
  parcela = valor / num
  parcela = round(parcela, 2)
  print (str(num) + "x de R$ " + str(parcela))