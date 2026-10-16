import os
os.system('cls')

numeros = []

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

print("Números na ordem digitada:")
for numero in numeros:
    print(numero)

print("Números na ordem inversa:")
for numero in reversed(numeros):
    print(numero)