import os
os.system('cls')

vetor_original = []
vetor_modificado = []

print("--- Leitura de 6 Números Inteiros ---")
for i in range(6):
    valor = int(input(f"Digite o {i+1}º número: "))
    vetor_original.append(valor)

for numero in vetor_original:
    if numero % 2 == 0:
        vetor_modificado.append(0)
    else:
        vetor_modificado.append(1)

print("\n================ RESULTADOS ================")
print(f"Vetor Antes:  {vetor_original}")
print(f"Vetor Depois: {vetor_modificado}")