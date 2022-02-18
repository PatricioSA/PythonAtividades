#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 18/11/2021
#Término: /11/2021
#Atividade007 - exercício g melhorado

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

#Validação
if (numero1 < 0 or numero2 < 0):
    print('Entrada inválida')
else:
    #Estrurura de repetição
    for c in range(numero1, numero2 + 1):
        divisores = 0

        for j in range(1, c + 1):
            if (c % j == 0):
                divisores += 1
        
        if (divisores == 2):
            soma += c
            print(c, end=' ')

#Saída
print()
print(f'A soma dos primos é {soma}')