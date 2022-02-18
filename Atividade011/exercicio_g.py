#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 07/02/2022
#Término: /02/2022

#Limpar o terminal
import os

#importando o módulo cálculos
from modulos.calculos import *


os.system('cls')

#Título
print('-'*80)
print('Operações matemáticas')
print('='*80)

#Início do Programa
while (True):
    print('1-Soma, 2-Subtração, 3-Produto, 4-Divisão, 5-Divisão inteira, 6-Resto '+ 
    ' da divisão')
    
    #Escolha da operação
    operacao = (input('Escolha o número correspondente a operação: '))
    
    #Validação da escolha
    if (not(operacao.isnumeric())):
        print('Inválido')
    else:
        operacao = int(operacao)
        if operacao != 1 and operacao != 2 and operacao != 3 and operacao != 4 and \
            operacao != 5 and operacao != 6:
            print('INVÁLIDO')
            print()
            continue
        else:
        #Valores a serem realizado a operação
            print()
            a = float(input('Digite o primeiro valor: '))
            b = float(input('Digite o segundo valor: '))

        #Condicionais que realizarão as operações
            if operacao == 1:
                resultado = soma(a, b)
                print(resultado)
            elif operacao == 2:
                resultado = subtracao(a, b)
                print(resultado)
            elif operacao == 3:
                resultado = produto(a, b)
                print(resultado)
            elif operacao == 4:
                resultado = divisao(a, b)
                print(resultado)
            elif operacao == 5:
                resultado = divisao_inteira(a, b)
                print(resultado)
            elif operacao == 6:
                resultado = resto_divisao(a, b)
                print(resultado)

    #Pergunta ao usuário de deseja rodar o programa novamente
    while (True):
        #entrada de dados
        pergunta = str(input('Deseja realizar outra operação? (s/n): ')).lower()

        #Validação da entrada de dados
        if (pergunta != 's') and (pergunta != 'n'):
            print('Inválido')
        elif pergunta == 's':
            break
        else:
            exit()