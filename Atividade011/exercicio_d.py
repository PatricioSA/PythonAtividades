#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 06/02/2022
#Término: /02/2022

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*80)
print('Fahrenheit para Célsius')
print('='*80)

def conversor_temperatura(fahrenheit):
    conversao = 5/9 * (fahrenheit - 32)

    return conversao

#Entrada de dados
fahrenheit= float(input('Digite a tamperatura: '))

#Invocando a função
conversao = conversor_temperatura(fahrenheit)

#Saída
print('-'*70)
print(f'Temperatura em Fahrenheit: {fahrenheit}')
print(f'A temperatura é de {conversao:.1f} °C')
print()