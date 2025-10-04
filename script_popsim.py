#!/usr/bin/env python3


pop_inicial = input("Digite o tamanho inicial da população: ")

while not pop_inicial.isdigit():
	print("Valor inválido. Por gentileza, digite um número inteiro positivo")
	pop_inicial = input("Digite o tamanho inicial da população: ")



taxa_cres = input("Digite a taxa de crescimento anual (em decimal): ")

while "." not in taxa_cres or not taxa_cres.replace(".","").isdigit():
	print("Valor inválido. Por gentileza, digite um valor decimal positivo. Por exemplo, 0.05 para 5% ao ano.")
	taxa_cres = input("Digite a taxa de crescimento anual (em decimal): ")



tempo = input("Digite o número de anos: ")

while not tempo.isdigit():
	print("Valor inválido. Por gentileza, digite um número inteiro positivo.")
	tempo = input("Digite o número de anos: ")



pop_final = int(pop_inicial)

for ano in range(1, int(tempo)+1):
	pop_final = pop_final * (1 + float(taxa_cres))
	print("Ano {}: {}".format(ano, pop_final))
