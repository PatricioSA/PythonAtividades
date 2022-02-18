#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 06/02/2022
#Término: /02/2022

#Limpar o terminal
import os
from math import pow
import re


os.system('cls')

def calculo_imc(peso=0.0, altura=0.0):

    #Calculo do imc
    imc = peso / pow(altura, 2)
    #Retorno valor do imc
    return imc

print('-'*70)
print('Calcular o IMC')
print('='*70)

try:
    peso = float(input('Informe o seu peso: '))
    altura = float(input('Informe sua altura: '))

    resultado = calculo_imc(peso, altura)

    print('-'*70)
    print(f'O cálculo do imc é igual a {resultado:.2f}')
    print('='*70)

except ValueError:
    print('Valor inválido')
    print('-'*70)
    print()

