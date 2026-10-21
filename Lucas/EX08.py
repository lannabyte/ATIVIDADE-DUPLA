import os
os.system('cls')

nomes = []
salarios = []

print("--- Cadastro de Funcionários ---")
for i in range(5):
    nome = input(f"Digite o nome do {i+1}º funcionário: ")
    salario = float(input(f"Digite o salário de {nome}: R$ "))
    
    nomes.append(nome)
    salarios.append(salario)

maior_salario = salarios[0]
nome_maior_salario = nomes[0]
qtd_acima_2000 = 0

for i in range(5):
    if salarios[i] > maior_salario:
        maior_salario = salarios[i]
        nome_maior_salario = nomes[i]
    
    if salarios[i] > 2000.00:
        qtd_acima_2000 += 1

print("\n================ RESULTADOS ================")
print(f"Funcionário com o maior salário: {nome_maior_salario} (R$ {maior_salario:.2f})")
print(f"Quantidade de funcionários que ganham acima de R$ 2.000,00: {qtd_acima_2000}")