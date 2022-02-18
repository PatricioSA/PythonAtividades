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
print('')
print('='*50)

#entrada de dados
nome = str(input('Digite seu nome completo: '))

#Cálculo
nomeQuebrado = nome.split()

#Saída
print(f'Seu primeiro nome separado é: {nomeQuebrado}')