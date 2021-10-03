# Exercicio 7
# Implemente um algoritmo que imprima a sequência de fibonacci. Pergunte para o usuário quantos números, da sequência de fibonacci, ele quer que sejam impressos. Ex: n = 6 
#1, 1, 2, 3, 5, 8

n = int(input("Quantos números você quer que sejam impressos?  "))

a = 0
b = 1
 
for i in range (n):
  print (b)
  aux = b 
  b = a + b
  a = aux

