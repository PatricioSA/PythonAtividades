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
print('PROGRAMA QUE MOSTRA O PRIMEIRO E ÚLTIMO NOME')
print('='*50)

#Entrada de dados
nomeCompleto = str(input('Digite seu nome completo: ')).strip()

nomeQuebrado = nomeCompleto.split()
primeiroNome = nomeQuebrado[0]
ultimoNome = nomeQuebrado[-1]

print(f'Seu primeiro nome é: {primeiroNome}')
print(f'Seu último nome é: {ultimoNome}')