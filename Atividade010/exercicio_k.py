#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 07/12/2021
#Término: /12/2021
#Faça um programa que peça continuamente o nome e a idade de uma pessoa. Caso o usuário digite a idade 999, 
#o programa será fi nal izado e executará uma impressão com os nomes cadastrados.

#Limpar o terminal
import os


os.system('cls')

print('='*80)

#declaração
nome = {}
listaNome = []


while (True):

    #Entrada de dados
    nome['Nome'] = str(input('Digite seu nome: '))
    nome['Idade'] = int(input('Digite sua idade: '))

    #copiando o dicionário
    listaNome.append(nome.copy())

    #Condicional
    if (nome['Idade'] == 999):
        break

os.system('cls')

#Saída
for nome in listaNome:
    for chave, valor in nome.items():
        print(f'{chave} : {valor}', end=' | ')