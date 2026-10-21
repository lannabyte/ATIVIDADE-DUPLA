import os
os.system('cls')

vetor = []
maiores_que_10 = 0

for i in range(10):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(num)
    if num > 10:
        maiores_que_10 += 1

soma = sum(vetor)

print("\n--- Resultados ---")
print("Vetor digitado:", vetor)
print("Soma de todos os elementos:", soma)
print("Quantidade de números maiores que 10:", maiores_que_10)