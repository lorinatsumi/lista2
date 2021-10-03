
#Exercicio 2
# Escreva um programa que permita ao usuário digitar 10 números quaisquer e ao final apresente o somatório e a média aritmética destes números.


soma = 0
n = 10
for num in range(n):
  valor = int(input("Digite o valor: "))
  soma = soma + valor


media = soma / n

print (soma)
print (media)