# Escreva um programa que imprima os n primeiros número primos. Peça para o usuário informar o valor de n.

def primo (x): 
  for i in range (2,x):
    if x %i==0:
      return False
  return True

print (primo (3))

n = int(input("Digite um número:  "))
x = 1

for i in range (n):
  while not primo (x):
    x = x + 1
  print (x)
  x = x + 1
