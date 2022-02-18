#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 04/11/2021
#Término: 05/11/2021
#Atividade004 - Exercício f

#Limpando terminal
import os
os.system('cls')

print('-'*30)
print('CÁLCULO DE ANO BISSEXTO ')
print('-'*30)

#Entrada de dados
ano = int(input('Digite um ano aleatório: '))

#Condicionais
if (ano <= 0):
    print('Ano Inválido')
elif (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto! ')

print()
print('Fim do Programa! ')