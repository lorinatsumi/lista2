# Exercicio 3
# Escreva um algoritmo para ler 10 números. Todos os números lidos com valor inferior a 40 devem ser somados. Escreva o valor final da soma efetuada.




n = 10
soma = 0

for valor in range(n):
  valor = int(input("Digite o valor: "))
  if valor < 40:
    x = valor
    soma = soma + x

print (soma)