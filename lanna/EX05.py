import os
os.system('cls')

notas = [0] * 5
soma = 0

for i in range(5):
    notas[i] = float(input(f"Nota {i+1}: "))
    soma = soma + notas[i]

media = soma / 5

acima = 0
for i in range(5):
    if notas[i] > media:
        acima = acima + 1

print("\nNotas:", notas)
print("Média:", media)
print("Notas acima da média:", acima)