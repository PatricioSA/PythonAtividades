#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 10/11/2021
#Término: /11/2021
#Atividade006 - exercício g

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*50)
print('')
print('='*50)

#Entrada de dados
numero = str(input('Digite um número milhar: '))

#Casting
numeroInteiro = int(numero)

#Cálculos
unidade = (numero // 1) % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

#Saída
print(f'O numero "{numero}" tem {unidade} unidades')
print(f'O numero "{numero}" tem {dezena} dezenas')
print(f'O numero "{numero}" tem {centena} centenas')
print(f'O numero "{numero}" tem {milhar} milhares')
print('-'*40)
print()