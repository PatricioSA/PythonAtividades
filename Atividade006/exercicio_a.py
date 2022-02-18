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
print('JUNTAR NOME')
print('='*50)

#Entrada de dados
nome = str(input('Digite seu primeiro nome: ')).title()
sobrenome = str(input('Digite seu sobrenome: ')).title()
ultimoNome = str(input('Digite seu últimonome: ')).title()

#Cálculo
nomeCompleto = nome + ' ' + sobrenome + ' ' + ultimoNome

#Saída
print(f'Seu nome completo é: {nomeCompleto}')