#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 04/11/2021
#Término: 05/11/2021
#Atividade004 - Exercício f

from datetime import date

import os


os.system('cls')

print('-'*30)
print('CÁLCULO DE ANO BISSEXTO ')
print('-'*30)

#Entrada de dados
ano = int(input('Digite um ano aleatório: '))
anoAtual = date.today().year

#Condicionais
if (ano <= 0):
    print('Ano Inválido')
elif (ano % 4 == 0) and (ano % 100 != 0) and (ano > anoAtual) or (ano % 400 == 0):
    print(f'O ano {ano} será bissexto')
elif (ano % 4 == 0) and (ano % 100 != 0) and (ano < anoAtual) or (ano % 400 == 0):
    print(f'O ano {ano} foi bissexto')
elif (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é bissexto')
else:
    if (ano < anoAtual):
        print(f'O ano {ano} não foi bissexto! ')
    elif (ano > anoAtual):
        print(f'O ano {ano} não será bissexto')
    else:
        print(f'O ano {ano} não é bissexto! ')

print()
print('Fim do Programa! ')