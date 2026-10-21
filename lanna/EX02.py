import os
os.system('cls')

dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
temperaturas = []

for i in range(7):
    temp = float(input(f"Digite a temperatura de {dias[i]}: "))
    temperaturas.append(temp)

media = sum(temperaturas) / len(temperaturas)
maior = max(temperaturas)
menor = min(temperaturas)

print("\n--- Relatório Semanal ---")
print("Temperaturas registradas:")
for i in range(7):
    print(f"  {dias[i]}: {temperaturas[i]:.1f}°C")

print(f"\nMédia semanal: {media:.1f}°C")
print(f"Maior temperatura: {maior:.1f}°C ({dias[temperaturas.index(maior)]})")
print(f"Menor temperatura: {menor:.1f}°C ({dias[temperaturas.index(menor)]})")