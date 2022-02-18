#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 09/10/2021
#Término: 09/10/2021
#Atividade005 - exercicio c

#Importando a biblioteca da função
from math import pow
import os


os.system('cls')

#Entrada de dados
base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))

#operação
potencia = pow(base, expoente)

#Saída
print(f'o número {base} elevado a {expoente} é: {potencia}')