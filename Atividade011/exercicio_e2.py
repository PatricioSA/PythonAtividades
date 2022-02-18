#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 06/02/2022
#Término: /02/2022

#Limpar o terminal
import os


os.system('cls')

def calculo_imc(peso=0.0, altura=0.0):
    #Cálculo do imc
    imc = peso / pow(altura, 2)

    #Condiciona
    if imc > 0 and imc <= 20:
        return imc, 'Magro'
    elif imc > 20 and imc <= 24.9:
        return imc, 'Peso Ideal'
    elif imc > 24.9 and imc <= 27:
        return imc, 'Sobrepeso'
    elif imc > 27 and imc <= 29.9:
        return imc, 'Obesidade leve'
    elif imc > 29.9 and imc <= 39.9:
        return imc, 'Obesidade'
    elif imc > 39.9 and imc <= 40:
        return imc, 'Obesidade Mórbida'

print('-'*70)
print('Calcular o IMC')
print('='*70)

try:
    peso = float(input('Informe o seu peso: '))
    altura = float(input('Informe sua altura: '))

    #Desempacotando
    resultado, situacao = calculo_imc(peso, altura)

    print('-'*70)
    print(f'O cálculo do imc é igual a {resultado:.2f}')
    print(f'Situação: {situacao}')
    print('='*70)

#Não é uma boa prática
except (ValueError, ZeroDivisionError, TypeError, NameError):

    print('Valor inválido!')
    print('-'*70)
    print()