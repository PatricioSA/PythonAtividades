#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 03/12/2021
#Término: /12/2021
#Atividade009 - exercicio b

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*70)
print('')
print('='*70)

tuplaNumeros = ()

while (True):
    numero = int(input('Digite um numero: '))
        
    listaNumero = list(tuplaNumeros)
    listaNumero.append(numero)
    tuplaNumeros = tuple(listaNumero)

    while (True):
        #Pergunta se deseja continuar
        continuar = input('Deseja continuar?: (s/n): ').lower()
    
        #Condicional
        while(continuar != 's') and (continuar != 'n'):               
            print('Digite "s" ou "n" ')
            continuar = input('Deseja continuar?: (s/n): ').lower()
        if (continuar == 's'):
            break
        else:
        
            #Saída
            print()
            print('Numeros: ', end=' ')
            for numero in tuplaNumeros:
                print(numero, end=' ')
            print()
    
            #Descobrir o índice do número
            numeroPosicao = int(input('Digite o valor que deseja saber a POSIÇÃO: '))
            while (numeroPosicao not in tuplaNumeros):
                print('NÚMERO NÃO ENCONTRADO')
                numeroPosicao = int(input('Digite o valor que deseja saber a POSIÇÃO: '))
            else:
                indice = tuplaNumeros.index(numeroPosicao)
                print(f'O número {numeroPosicao} aparece pela 1º vez na posição {indice}')
        
            print()
        
            #Descobrir quantas vezes o número aparece
            numeroContar = int(input('Digite o número que deseja saber sua ocorrência: '))
            while (numeroContar not in tuplaNumeros):
                print('NÚMERO NÃO ENCONTRADO')
                numeroContar = int(input('Digite o número que deseja saber sua ocorrência: '))
            else:
                contar = tuplaNumeros.count(numeroContar)
                print(f'O número {numeroContar} aparece {contar} vezes')
                print()
            exit()