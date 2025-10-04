#!/usr/bin/env python3

import sys

seq_dna = sys.argv[1]

if not seq_dna.isalpha():
	print("Dados inválidos. Por gentileza, certifique-se que o primeiro argumento contém apenas caracteres alfabéticos.")
	sys.exit(1)

n1 = sys.argv[2]
n2 = sys.argv[3]
n3 = sys.argv[4]
n4 = sys.argv[5]
n5 = sys.argv[6]
n6 = sys.argv[7]


if not n1.isdigit() or not n2.isdigit() or not n3.isdigit() or not n4.isdigit() or not n5.isdigit() or not n6.isdigit():
	print("Dados inválidos. Por gentileza, certifique-se que os argumentos 2 a 7 contém apenas números inteiros")
else:
	n1 = int(n1)
	n2 = int(n2)
	n3 = int(n3)
	n4 = int(n4)
	n5 = int(n5)
	n6 = int(n6)

tam_seq = len(seq_dna)

if n1>tam_seq or n2>tam_seq or n3>tam_seq or n4>tam_seq or n5>tam_seq or n6>tam_seq:
	print("Dados inválidos. Por gentileza, certifique-se que os valores dos argumentos 2 a 7 são menores que o tamanho do argumento 1. \nCaso vá utilizar a mesma sequência, o valor máximo é igual a {}.".format(tam_seq))
else:
	cds1_cds2 = seq_dna[n2:n3-1]
	print(cds1_cds2)
	if not cds1_cds2.startswith("GT") or not cds1_cds2.endswith("AG"):
		print("A sequência entre CDS 1 e CDS 2 não começa com os nucleotídeos GT e/ou não termina com os nucleotídeos AG.")
	else:
		cds2_cds3 = seq_dna[n4:n5-1]
		if not cds2_cds3.startswith("GT") or not cds2_cds3.endswith("AG"):
			print("A sequência entre CDS 2 e CDS 3 não começa com os nucleotídeos GT e/ou não termina com os nucleotídeos AG.")
		else:
			print(seq_dna[n1-1:n2]+seq_dna[n3-1:n4]+seq_dna[n5-1:n6])

