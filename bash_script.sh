#!/bin/bash

#Exercício 2

#O conteúdo desse script contempla:

#Um comando que mostre a pasta/diretório onde você está:
echo "Diretório atual: $(pwd)"  #O comando 'pwd' mostra o diretório atual
#O comando 'echo' foi utilizado para deixar a saída mais organizada e legível, sendo uma escolha mais didática do que simplesmente executar 'pwd' isoladamente.


#Um comando que gere uma lista com detalhes do conteúdo da sua pasta HOME e redirecione essa lista para o arquivo: lista_HOME.txt
ls -l ~ > lista_HOME.txt  # O comando 'ls' lista o conteúdo de um diretório; a opção '-l' exibe informações detalhadas; e '~' representa a pasta HOME.
#A parte '> lista_HOME.txt' redireciona a saída do comando para o arquivo especificado, criando ou sobrescrevendo o arquivo 'lista_HOME.txt' com o resultado da listagem.


#Um comando que imprima a data atual na tela:
echo "Data e hora atuais: $(date)" #O comando 'date' imprime a data e hora atuais do sistema.
#Novamente, o 'echo' foi utilizado para formatar melhor a saída, tornando-a mais clara e informativa do que o uso isolado de 'date'.
