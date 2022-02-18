#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 10/11/2021
#Término: 12/11/2021
#Atividade006 - exercício c

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*50)
print('')
print('='*50)

#Entrada de dados
nome = str(input('Digite seu nome: ')).title()

#
if ('Oliveira' in nome):
    print('Olá Oliveira! ')
else:
    print(f'Neste nome tem "Oliveira"?: Não')

print('-'*50)
print()