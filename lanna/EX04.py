import os
os.system('cls')

vetor = []

for i in range(8):
    numero = int(input(f"Digite a posição do {i+1}º número: "))
    vetor.append(numero)

pesquisa = int(input("\nDigite um número para pesquisar: "))

if pesquisa in vetor:
    posicao = vetor.index(pesquisa)
    print(f"O número {pesquisa} foi encontrado na posição {posicao}.")
else:
    print("Número não encontrado.")