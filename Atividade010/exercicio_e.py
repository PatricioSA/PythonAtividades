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
ferramentas = {}
listaFerramentas = []

for c in range(0, 5):

    #Entrada de dados
    ferramentas['Ferramenta'] = str(input('Digite a ferramenta: '))

    #Cópia do dicionário
    listaFerramentas.append(ferramentas.copy())

    tamanho = len(listaFerramentas)
print()

#Saída
for ferramentas in listaFerramentas:
    for chave, valor in ferramentas.items():
        print(f'{chave} : {valor}')
print(f'A quantidade de elemetos é: {tamanho}')