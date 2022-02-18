#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 10/11/2021
#Término: 12/11/2021
#Atividade006 - exercício a

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*50)
print('TROCA DE NOME "SILVA" PARA "OLIVEIRA"')
print('='*50)

#Declarações
nome = 'João da Silva'

#Cálculo
nomeNovo = nome.replace('da Silva', 'de Oliveira')

#Saída
print(f'O nome é: {nome}')
print(f'O nome novo é: {nomeNovo}')
print('-'*50)
print()