#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 15/02/2022
#Término: 15/02/2022

'''
1. Soma
2. Subtração
3. Produto
4. Divisão
5. Divisão inteira
6. Resto da divisão

'''

#Limpar o terminal
import os

from Atividade011.modulos.calculos import resto_divisao


os.system('cls')

def calculos(numero_1, numero_2, escolha):
    if escolha == 1:
        soma = numero_1 + numero_2
        return '+', soma
    elif escolha == 2:
        subtracao = numero_1 - numero_2
        return '-', subtracao
    elif escolha == 3:
        produto = numero_1 * numero_2
        return '*', produto
    elif escolha == 4:
        if numero_2 == 0:
            return '/', 'Impossível dividir por zero!'
        else:
            resto_divisao = numero_1 % numero_2
            return '%', resto_divisao

while True:
    print('''
        1. Soma
        2. Subtração
        3. Divisão
        4. Divisão
        5. Divisão inteira
        6. Resto da divisão
        7. Sair
    ''')

    try:
        escolha = int(input('Escolha uma operação (1-7): '))

        if escolha == 7:
            break
        else:
            numero_1 = float(input('Entre com o 1º número: '))
            numero_2 = float(input('Entre com o 2° número: '))

            #operador, resultado = calculos(numero_1)
