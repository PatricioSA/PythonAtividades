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
alunos = {'nome': 'John', 'idade': 40, 'peso': 80, 'altura': 1.70}
listaAlunos = []

listaAlunos.append(alunos.copy())

#Saída com for
for alunos in listaAlunos:
    print()
    for chave, valor in alunos.items():
        print(f'{chave} : {valor}')

#Deletando uma chave
apagar = str(input('Qual chave deseja apagar: ')).lower()
del(alunos[apagar])

print()
for chave, valor in alunos.items():
    print(f'{chave} : {valor}')

print()
print(listaAlunos)









#for i, valor in enumerate(listaAlunos):
    #print(f'Registro {i} : {valor}')