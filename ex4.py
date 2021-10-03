# Exercicio 4
# Faça um algoritmo que calcule e escreva a média aritmética dos números inteiros entre 15 (inclusive) e 100 (inclusive).



soma = 0
contador = 0

for valor in range(15,101):
    soma = soma + valor 
    contador = contador + 1


media = soma / contador

print (media)
print (contador)
