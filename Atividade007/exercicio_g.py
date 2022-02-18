#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 18/11/2021
#Término: /11/2021
#Atividade007 - exercício g

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*60)
print('IMPRIME OS NÚMEROS PRIMOS NO INTERVALO DETERMINADO E SOMA-OS')
print('='*60)

print()

#Entrada de dados
numero1 = int(input('Digite o início do intervalo: '))
numero2 = int(input('Digite o final do intervalo: '))
soma = 0

#Estrurura de repetição
for c in range(numero1, numero2):

    if (c % 2 != 0) and (c % 3 != 0) and (c % 5 != 0) and (c % 7 != 0) and (c % 11 != 0):
        
        #Soma os números primos
        soma += c
        
        print(f'Número {c}')
    
    elif (c == 2) or (c == 3) or (c == 5) or (c == 7) or (c == 11):
        
        #Soma os números primos
        soma += c
        
        print(f'Número {c}')

#Saída
print(f'A soma dos primos é {soma}')