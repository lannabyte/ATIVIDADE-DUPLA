import os
os.system

print("--- LEITURA DE IDADES ---")

idades = [0] * 5

for i in range(5):
    valida = False
    
    while not valida:
        idade = int(input(f"Digite a idade da {i + 1}ª pessoa (0 a 120): "))
        
        if idade >= 0 and idade <= 120:
            idades[i] = idade
            valida = True
        else:
            print("Idade inválida! Digite um valor entre 0 e 120.\n")

maior_idade = idades[0]
menor_idade = idades[0]
qtd_maiores = 0

for i in range(5):
    if idades[i] > maior_idade:
        maior_idade = idades[i]
        
    if idades[i] < menor_idade:
        menor_idade = idades[i]
        
    if idades[i] >= 18:
        qtd_maiores = qtd_maiores + 1

print("\n--- RESULTADOS ---")
print(f"Vetor com as idades: {idades}")
print(f"Maior idade: {maior_idade}")
print(f"Menor idade: {menor_idade}")
print(f"Quantidade de maiores de idade (>= 18): {qtd_maiores}")