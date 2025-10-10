#!/usr/bin/env python3

#Questão 4
#Objetivo: Calcular o crescimento de uma população ao longo de um determinado período de tempo, considerando uma taxa de crescimento anual constante informada pelo usuário.



#Recebendo o tamanho inicial da população a partir da entrada do usuário.
pop_inicial = input("Digite o tamanho inicial da população: ")

#Enquanto o valor informado não for um número inteiro positivo, solicita novamente.
while not pop_inicial.isdigit():
	print("Valor inválido. Por gentileza, digite um número inteiro positivo")
	pop_inicial = input("Digite o tamanho inicial da população: ")


#Recebendo a taxa de crescimento anual.
taxa_cres = input("Digite a taxa de crescimento anual (em decimal): ")

#Verifica se a taxa contém um ponto decimal e se todos os demais caracteres são dígitos - garante que o valor seja um número positivo com ponto.
while "." not in taxa_cres or not taxa_cres.replace(".","").isdigit():
	print("Valor inválido. Por gentileza, digite um valor decimal positivo. Por exemplo, 0.05 para 5% ao ano.")
	taxa_cres = input("Digite a taxa de crescimento anual (em decimal): ")


#Recebendo o número de anos a serem simulados.
tempo = input("Digite o número de anos: ")

#Garantindo que o número de anos seja um inteiro positivo.
while not tempo.isdigit():
	print("Valor inválido. Por gentileza, digite um número inteiro positivo.")
	tempo = input("Digite o número de anos: ")


#Convertendo o valor inicial da população para inteiro para realizar os cálculos.
pop_final = int(pop_inicial)

#Calculando a posição a cada ano, aplicando a taxa de crescimento acumulativamente.
for ano in range(1, int(tempo)+1):
	pop_final = pop_final * (1 + float(taxa_cres))  #Aplica o crescimento percentual anual sobre o valor atual da população.
	print("Ano {}: {}".format(ano, pop_final))  #Exibe o tamanho da população ao final de cada ano.
