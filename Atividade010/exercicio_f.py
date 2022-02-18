#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 07/12/2021
#Término: /12/2021

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*80)
print('')
print('='*80)

#Declaração
vinhos = {}
listaVinhos = []

for c in range(0, 2):

    #Entrada de dados
    vinhos['Nome'] = str(input('Nome do vinho: '))
    vinhos['Tipo'] = str(input('Tipo: '))
    vinhos['Teor alcoolico'] = str(input('Teor alcoolico: '))
    vinhos['Ano'] = int(input('Ano: '))
    print()

    #Cópia do dicionário
    listaVinhos.append(vinhos.copy())

print()

#Saída
for vinhos in listaVinhos:
    print()
    for chave, valor in vinhos.items():
        print(f'{chave} : {valor}')