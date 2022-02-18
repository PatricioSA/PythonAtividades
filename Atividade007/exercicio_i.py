#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 19/11/2021
#Término: 19/11/2021
#Atividade007 - exercicio i

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*50)
print('ESTOU EM LOOPING')
print('='*50)

print()

#Estrutura de repetição
while (True):

    #Entrada
    programa = str(input('Estou em looping [f - Finalizar]: ')).lower()

    #Condicional
    if (programa != 'f'):
        print('Ainda estou em looping...')
    else:
        print('-'*50)
        print('Você digitou "f", o programa foi finalizado!')

        #interrompe o laço
        break

print('-'*50)
print()