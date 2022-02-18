#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 10/11/2021
#Término: /11/2021
#Atividade006 - exercício h

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*50)
print('OCORRÊNCIA DO DA LETRA "O" NO NOME')
print('='*50)

#Entrada de dados
nome = str(input('Digite o nome: ')).lower()

#Declaração
ocorrencias = nome.count('o')
posicao = nome.find('o')
posicao2 = nome.rfind('o')

print(f'O nome é: {nome}')
print(f'A letra "o" aparece {ocorrencias} vezes')
print(f'A letra "o" aparece na posição {posicao} na primeira vez')
print(f'A letra "o" aparece na posição {posicao2} na última vez')