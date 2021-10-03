#Diz a lenda que o criador do jogo de xadrez solicitou como pagamento ao rei um grão de arroz para a primeira casa do tabuleiro, dois para a segunda, quatro para a terceira, oito para a quarta, dezesseis para a quinta e assim por diante, até a sexagésima quarta casa do tabuleiro. A cada casa o valor de grãos é dobrado. Escreva um programa que calcule os seguintes valores, apresentando todos os resultados em números inteiros:

#• Quantos grãos de arroz seriam necessários para efetuar este pagamento.

n = 1

for i in range (64):
  n = (n + n)

print (n)

#• Quantos quilos de arroz seriam necessários (um quilo de arroz tem aproximadamente 170 mil grãos).

quilo = (n/170000)

print (str (quilo) + " quilos")


#• Quantos quilômetros quadrados seria necessário cultivar para produzir essa quantidade de arroz (um quilômetro quadrado produz aproximadamente 550 mil quilos de arroz).

quilometros = (quilo/550000)

print (str(quilometros) + " quilometros")

#• Quantas vezes o território brasileiro teria que ser cultivado para produzir essa quantidade de arroz (o território brasileiro tem 8.514.876 quilômetros quadrados)

vezes = (quilometros / 8514876)

print ("Seria necessário " + str(vezes) + " vezes")
