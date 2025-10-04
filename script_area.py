#!/usr/bin/env python3

# Questão 3

import sys  #Importando o módulo necessário para ler argumentos passados pelo terminal


#Recebendo os valores dos catetos a partir da linha de comando (fornecidos pelo usuário)
catetoA = sys.argv[1]
catetoB = sys.argv[2]


#Definindo as condições de valores inválidos: não inteiros ou maiores/iguais a 500.
A_invalido = not catetoA.isdigit() or int(catetoA)>=500  #Define a invalidade para o valor do cateto A.
B_invalido = not catetoB.isdigit() or int(catetoB)>=500  #Define a invalidade para o valor do cateto B.
#Resolvi adicionar as regras de invalidade como variáveis pois o bloco de códigos a seguir estava ficando mais extenso do que
#o necessário, visto que para cada condição eu escrevia novamente as condições.


#Verifica quais valores são inválidos e imprime mensagens apropriadas
if A_invalido and B_invalido:  #Ambos os valores são inválidos
	print("Valores inválidos digitados para ambos os catetos. \nPor gentileza, digite números inteiros menores que 500.")
#Em um primeiro momento, eu havia colocado esse primeiro bloco "if" como o último "elif", porém seria um bloco inútil, visto
#que nunca as outras condições já seriam verdadeiras antes dessa chegar.
elif A_invalido:  #Apenas o valor do cateto A é inválido
	print("Valor inválido digitado para o cateto A.\nPor gentileza, digite um número inteiro menor que 500.")
elif B_invalido:  #Apenas o valor do cateto B é inválido
	print("Valor inválido digitado para o cateto B. \nPor gentileza, digite um número inteiro menor que 500.")
else:
	#Caso ambos os valores sejam válidos, a área é calculada e mostrada ao usuário
	area = (int(catetoA)*int(catetoB))/2  #Calcula a área do triângulo. Nota-se a necessidade de transformar a string do cateto em um inteiro para o cálculo.
	print("A área do triângulo retângulo com lados a={} e b={}, é {}".format(catetoA, catetoB, area))
