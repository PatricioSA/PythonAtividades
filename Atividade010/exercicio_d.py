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
cores = {}
cor = []

for c in range(0, 5):

    #Entrada de dados
    cores['cor'] = str(input('Digite a cor: '))

    #Cópia do dicionário
    cor.append(cores.copy())
print()

#Saída
for cores in cor:
    for chave, valor in cores.items():
        print(f'{chave} : {valor}')