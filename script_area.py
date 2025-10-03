#!/usr/bin/env python3

# Questão 3

import sys

catetoA = int(sys.argv[1])
catetoB = int(sys.argv[2])

if isdigit(catetoA)==False or catetoA>=500:
	print("Valor inválido digitado para o cateto A")


area = (catetoA*catetoB)/2

print("A área do triângulo retângulo com lados a={} e b={}, é {}".format(catetoA, catetoB, area))
