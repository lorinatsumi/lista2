# Exercicio 6
# Faça um programa que leia 5 valores e no final, escreva o maior e o menor valor lido. 

maior = 0
menor = 9999999999999
n = 5

for valor in range(n):
  valor = int(input("Digite o valor: "))
  if valor > maior:
    maior = valor
  if valor < menor:
    menor = valor   

print ("O maior é: " + str(maior))

print ("O menor é: " +str(menor))