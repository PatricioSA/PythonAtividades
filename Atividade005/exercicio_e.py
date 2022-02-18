#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 09/10/2021
#Término: 09/10/2021
#Atividade005 - exercicio e

#Importando a biblioteca da função
from random import randint
import os


os.system('cls')

#Título
print('-'*30)
print('SORTEIO DE NÚMEROS')
print('-'*30)

#Declaração
Aleatorio = randint(1, 20)

#Saída
print(f'O numero sorteado é: {Aleatorio}')

print()