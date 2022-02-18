#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 26/11/2021
#Término: /11/2021
#Atividade008 - exercicio k
#

#Limpar o terminal
import os


os.system('cls')

listaNomes = []

for c in range(0, 6):

    #Entrada de dados
    nome = input('Digite um nome: ').capitalize()
    listaNomes.append(nome)

if ('Pedro' in listaNomes):
    print(listaNomes)
    posicao = listaNomes.index('Pedro')
    print(f'O nome está na posição {posicao}')
else:
    print()
    print('O elemento não consta na listagem!')
    print()
    
