#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 10/11/2021
#Término: 12/11/2021
#Atividade008 - exercício e

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*50)
print('CONTANDO VOGAIS')
print('='*50)

#Entrada de dados
listaVogais = []
frase = str(input('Digite uma frase: ')).lower()

#Cálculos
quebra = frase.split()
vogalA = frase.count('a')
vogalE = frase.count('e')
vogalI = frase.count('i')
vogalO = frase.count('o')
vogalU = frase.count('u')
vogais = frase.count('a') + frase.count('e')

listaVogais.append(frase.count('a'))
print(listaVogais)