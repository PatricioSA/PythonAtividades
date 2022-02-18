#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 26/11/2021
#Término: /11/2021
#Atividade008 - exercicio d
#Faça um programa que leia 5 nomes, depois imprima estes nomes com seus respectivos índices.

#Limpar o terminal
import os


os.system('cls')

print('-'*70)
print('')
print('='*70)

#Criando uma lista
listaAluno = []

for c in range(0, 5):
    nome = str(input(f'Digite o {c+1}º nome: ')).capitalize()
    listaAluno.append(nome)

for i, numero in enumerate(listaAluno):
    print(f'Indice: {i} Nome: {numero}')