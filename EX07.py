import os
os.system('cls')

vetor_origem = []
vetor_positivos = []

print("--- Leitura de 10 Números Inteiros ---")
for i in range(10):
    valor = int(input(f"Digite o {i+1}º número: "))
    vetor_origem.append(valor)

for numero in vetor_origem:
    if numero > 0:
        vetor_positivos.append(numero)

print("\n================ RESULTADOS ================")
print(f"Vetor Original: {vetor_origem}")
print(f"Vetor de Positivos: {vetor_positivos}")
print(f"Quantidade de elementos copiados: {len(vetor_positivos)}")