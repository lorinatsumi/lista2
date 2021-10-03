#Lista 2
# Exercicio 1
#  Ler 10 valores e escrever quantos desses valores lidos são NEGATIVOS. 

n = 10
soma = 0

for valor in range(n):
  valor = int(input("Digite o valor: "))
  if valor < 0:
    valor = 1
    soma = soma + valor

print (soma)

