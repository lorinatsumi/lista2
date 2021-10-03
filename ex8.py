# Implemente um algoritmo que leia um número inteiro, em seguida calcule o fatorial deste número e apresente para o usuários.
#Ex: n = 4
#O Fatorial de 4 é 24


n = int(input("Digite um número:  "))

fatorial = 1

for i in range (n):
  fatorial = fatorial * n
  n = n - 1

print(fatorial)