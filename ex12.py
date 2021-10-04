#Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o preço unitário. 
#Calcular e escrever o total (total = quantidade adquirida * preço unitário), o desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que: 
#Se quantidade <= 5 o desconto será de 2% 
#Se quantidade > 5 e quantidade <=10 o desconto será de 3%  
#Se quantidade > 10 o desconto será de 5% 


produto = input("Digite o produto: ")
quantidade = int(input("Digite a quantidade: "))
preco = int(input("Digite o preço: "))

total = quantidade * preco

print (total)

if quantidade <= 5:
  desconto = 2/100

if quantidade > 5 and quantidade <=10:
  desconto = 2/100

if quantidade > 10:
  desconto = 5/100

print (desconto)

totalapagar = total - (total*desconto)

print (totalapagar)