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
alunos = {}
listaAlunos = []

for c in range(0, 2):

    #Entrada de dados
    alunos['Nome'] = str(input('Digite o nome: '))
    alunos['Data nascimento'] = str(input('Digite o nascimento: '))
    alunos['Matrícula'] = int(input('Digite a matrícula: '))
    
    print()

    #Cópia do dicionário
    listaAlunos.append(alunos.copy())
print()

#Saída
for alunos in listaAlunos:
    print()
    for chave, valor in alunos.items():
        print(f'{chave} : {valor}')