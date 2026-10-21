import os
os.system ('cls')

vetor_a = []
vetor_b = []
vetor_c = []

print("--- Leitura do Vetor A ---")
for i in range(5):
    valor = int(input(f"Digite o {i+1}º número do Vetor A: "))
    vetor_a.append(valor)

print("\n--- Leitura do Vetor B ---")
for i in range(5):
    valor = int(input(f"Digite o {i+1}º número do Vetor B: "))
    vetor_b.append(valor)

for i in range(5):
    soma = vetor_a[i] + vetor_b[i]
    vetor_c.append(soma)

print("\n================ RESULTADOS ================")
print(f"Vetor A: {vetor_a}")
print(f"Vetor B: {vetor_b}")
print(f"Vetor C (A + B): {vetor_c}")