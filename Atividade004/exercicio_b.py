#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 04/11/2021
#Término: 04/11/2021
#Atividade004 - Exercício b

#Limpando terminal
import os
os.system('cls')

print('-'*30)
print('QUAL É O MAIOR E O MENOR ? ')
print('-'*30)

#Entrada de dados
numeroUm = int(input('Digite o 1º valor: '))
numeroDois = int(input('Digite o 2º valor: '))
numeroTres = int(input('Digite o 3º valor: '))

#Condicionais
if (numeroUm > numeroDois) and (numeroUm > numeroTres):
    print(f'{numeroUm} é o MAIOR')
elif (numeroDois > numeroUm) and (numeroDois > numeroTres):
    print(f'{numeroDois} é o MAIOR')
elif (numeroTres > numeroUm) and (numeroTres > numeroDois):
    print(f'{numeroTres} é o MAIOR')

if (numeroUm < numeroDois) and (numeroUm < numeroTres):
    print(f'{numeroUm} é o MENOR')
elif (numeroDois < numeroUm) and (numeroDois < numeroTres):
    print(f'{numeroDois} é o MENOR')
elif (numeroTres < numeroUm) and (numeroTres < numeroDois):
    print(f'{numeroTres} é o MENOR')

print()
print('Fim do Progama')