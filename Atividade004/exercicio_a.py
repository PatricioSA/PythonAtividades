#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 04/11/2021
#Término: /11/2021
#Atividade004 - Exercício a

#Limpando terminal
import os
os.system('cls')

print('-'*30)
print('É PAR OU IMPAR ? ')
print('-'*30)

#Entrada de dados
numero = int(input('Digite um valor inteiro: '))

#Condicionais
if (numero % 2 == 0):
    print(f'{numero} é par! ')
else:
    print(f'{numero} é impar! ')

print()
print('Fim do Programa')