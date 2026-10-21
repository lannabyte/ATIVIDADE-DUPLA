import os
os.system('cls')

vetor = []

for i in range(1, 6):
    num = int(input(f"Digite o {i}º número inteiro: "))
    vetor.append(num)

print("\nOrdem digitada:", *vetor)

vetor.reverse()
print("Ordem inversa:", *vetor)