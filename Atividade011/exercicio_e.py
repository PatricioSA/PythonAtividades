#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 06/02/2022
#Término: /02/2022

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*80)
print('')
print('='*80)

def conversor_temperatura(peso, altura):
    calculo = peso / altura ** 2
    
    return calculo
 
#Entrada de dados
peso = float(input('Digite peso: ')) 
altura = float(input('Digite a altura: '))

calculo = conversor_temperatura(peso, altura)

print(f'O IMC é: {calculo:.1f}')