#Implemente um programa que apresente para o usuário se é mais vantajoso abastecer com álcool ou gasolina. Leia o valor do litro de álcool e o valor do litro de gasolina. Se o valor do litro de álcool vou menor que 70% do valor do litro de gasolina, é mais vantajoso álcool, e caso contrário será mais vantajoso abastecer com gasolina.



alcool = float (input("Digite o valor do litro do álcool: "))

gasolina = float (input("Digite o valor do litro da gasolina: "))

if alcool < (gasolina - (gasolina*0.3)):
  print ("O álcool é mais vantajoso")
else:
  print ("A gasolina é mais vantajosa")




