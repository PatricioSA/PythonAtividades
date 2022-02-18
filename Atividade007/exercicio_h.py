#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 17/11/2021
#Término: 17/11/2021
#Atividade007 - exercicio h

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*50)
print('')
print('='*50)

print()

#Entrada de dados
inicio = input('Digite o início do intervalo: ')
fim = input('Digite o fim do intervalo: ')
numero1 = input('Digite o 1º numero a ser ignorado: ')
numero2 = input('Digite o 2º numero a ser ignorado: ')
numero3 = input('Digite o 3º numero a ser ignorado: ')

#Condicional
if (not(inicio.isnumeric()) or not(fim.isnumeric()) or
    not(numero1.isnumeric()) or not(numero2.isnumeric() or 
    not(numero3.isnumeric()))):
    print(f'Valores Inválido')
else:
    #Casting das variáveis
    inicio = int(inicio)
    fim = int(fim)
    numero1 = int(numero1)
    numero2 = int(numero2)
    numero3 = int(numero3)

    #Estrutura de Repetição
    for c in range(inicio, fim):
        if (c == numero1 or c == numero2 or c == numero3):
            continue
        else:
            print(f'Número {c}')
