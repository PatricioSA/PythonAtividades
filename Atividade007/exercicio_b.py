#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 18/11/2021
#Término: 19/11/2021
#Trabalhando com For

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*50)
print('ESTRUTURA DE REPETIÇÃO FOR RANGE')
print('='*50)

print()

#Entrada de dados
inicio = (input('Digite o início do intervalo: '))
fim = (input('Digite o fim do intervalo: '))

#Condicional
if (not(inicio.isnumeric()) or not(fim.isnumeric())):
    print(f'Valor Inválido')
else:
    inicio = int(inicio)
    fim = int(fim)
    
    #Estrutura de repetição
    for c in range(inicio, fim):
        print(c + 1, end=' ')