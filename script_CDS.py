#!/usr/bin/env python3

#Questão 5

import sys  #Importa o módulo sys para permitir a leitura de argumentos passados via linha de comando.

#Verificando se o usuário forneceu exatamente 7 argumentos (além do nome do script).
if len(sys.argv) != 8:
    print("Por favor, insira a sequência de DNA seguida de seis coordenadas numéricas.")
    sys.exit(1)


#Recebendo a sequência de DNA como o primeiro argumento fornecido pelo usuário:
seq_dna = sys.argv[1]

#Verificando se a sequência contém apenas caracteres alfabéticos:
if not seq_dna.isalpha():
	print("Dados inválidos. Por gentileza, certifique-se que o primeiro argumento contém apenas caracteres alfabéticos.")
	sys.exit(1)  #Encerra o programa caso o dado seja inválido. Como não há a utilização de input(), não há como pedir novamente ao usuário enquanto sua entrada não atender os requisitos, como fiz no exercício 4.


#Recebendo os seis argumentos seguintes, correspondentes às posições dos limites das CDS.
n1 = sys.argv[2]
n2 = sys.argv[3]
n3 = sys.argv[4]
n4 = sys.argv[5]
n5 = sys.argv[6]
n6 = sys.argv[7]

#Verifica se todos os seis valores fornecidos são inteiros.
if not n1.isdigit() or not n2.isdigit() or not n3.isdigit() or not n4.isdigit() or not n5.isdigit() or not n6.isdigit():
	print("Dados inválidos. Por gentileza, certifique-se que os argumentos 2 a 7 contém apenas números inteiros")
else:
	#Converte os valores para inteiros, caso sejam válidos, permitindo o uso em operações de fatiamento.
	n1 = int(n1)
	n2 = int(n2)
	n3 = int(n3)
	n4 = int(n4)
	n5 = int(n5)
	n6 = int(n6)

#Calculando o tamanho da sequência, para validar os índices.
tam_seq = len(seq_dna)

#Verificando se algum dos índices fornecidos excede o tamanho da sequência.
if n1>tam_seq or n2>tam_seq or n3>tam_seq or n4>tam_seq or n5>tam_seq or n6>tam_seq:
	print("Dados inválidos. Por gentileza, certifique-se que os valores dos argumentos 2 a 7 são menores que o tamanho do argumento 1. \nCaso vá utilizar a mesma sequência, o valor máximo é igual a {}.".format(tam_seq))
else:
	#Obtendo a sequência localizada entre CDS 1 e CDS 2.
	#Essa região corresponde ao intron 1, ou seja, a parte NÃO codificante entre CDS1 e CDS2.
	#Subtraí 1 de n3 para garantir que a base inicial da próxima CDS (posição n3) não seja incluída no fatiamento.
	cds1_cds2 = seq_dna[n2:n3-1]

	#Verificando se essa região começa com 'GT' e termina com 'AG'.
	if not cds1_cds2.startswith("GT") or not cds1_cds2.endswith("AG"):
		print("A sequência entre CDS 1 e CDS 2 não começa com os nucleotídeos GT e/ou não termina com os nucleotídeos AG.")
	else:
		#Caso a primeira verificação passe, realiza a mesma checagem entre CDS 2 e CDS 3.
		# Essa região corresponde ao intron 2.
		cds2_cds3 = seq_dna[n4:n5-1]
		if not cds2_cds3.startswith("GT") or not cds2_cds3.endswith("AG"):
			print("A sequência entre CDS 2 e CDS 3 não começa com os nucleotídeos GT e/ou não termina com os nucleotídeos AG.")
		else:
			# Se todas as verificações forem bem-sucedidas, imprime a sequência concatenada das três CDS.
			# Cada CDS é obtida com base nas posições fornecidas: [n1-1:n2], [n3-1:n4], [n5-1:n6].
			# Subtraí 1 do início de cada CDS porque, em Python, os índices começam em 0,enquanto na Biologia as posições de nucleotídeos geralmente são contadas a partir de 1.
			# Assim, o fatiamento reflete corretamente as coordenadas biológicas fornecidas pelo usuário.
			print("Concatenação das CDS: \n{}".format(seq_dna[n1-1:n2]+seq_dna[n3-1:n4]+seq_dna[n5-1:n6]))  # Adicionei o texto apenas para deixar a saída melhor organizada e mais informativa.
