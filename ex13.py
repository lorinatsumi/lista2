#Faça um algoritmo para ler as 3 notas obtidas por um aluno. Calcular a média de aproveitamento e escreva o conceito do aluno de acordo com a tabela de conceitos mais abaixo:

nota1 = int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota: "))
nota3 = int(input("Digite sua terceira nota: "))

media = ((nota1 + nota2 + nota3)/3)


if media >= 9:
  print ("Conceito A")

if media >= 7.5 and media < 9:
  print ("Conceito B")

if media >= 6 and media < 7.5:
  print ("Conceito C")

if media < 6:
  print ("Conceito D")


