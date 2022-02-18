#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 26/11/2021
#Término: /11/2021
#Atividade008 - exercicio m
#Faça um programa que gere 10 números aleatórios. Após gerar esses números, crie duas listas novas com ordenação ascendente e descendente.

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*70)
print('Listas')
print('='*70)

#Criando as listas
listaNumero = []
listaAscendete = []
listaDescendente = []

for c in range(0, 10):
    numero = int(input(f'Digite o {c+1}º número: '))
    listaNumero.append(numero)

#Ordenando as listas
listaAscendete = sorted(listaNumero)
listaDescendente = sorted(listaNumero, reverse=True)

#Saída
print()
print(f'A lista é: {listaNumero}')
print(f'Lista em ordem ascendente: {listaAscendete}')
print(f'Lista em ordem descendente: {listaDescendente}')
print()