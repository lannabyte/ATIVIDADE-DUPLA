import os
os.system

temperaturas = []
dias_da_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

for dia in dias_da_semana:
    temp = float(input(f"Digite a temperatura de {dia}: "))
    temperaturas.append(temp)

media = sum(temperaturas) / len(temperaturas)
maior = max(temperaturas)
menor = min(temperaturas)

print("\n--- RESULTADOS DA SEMANA ---")
print("Temperaturas registradas:")
for i in range(7):
    print(f"- {dias_da_semana[i]}: {temperaturas[i]}°C")

print(f"\nMédia da semana: {media:.1f}°C")
print(f"Maior temperatura: {maior}°C")
print(f"Menor temperatura: {menor}°C")