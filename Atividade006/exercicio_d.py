#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 10/11/2021
#Término: /11/2021
#Atividade006 - exercício d

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*50)
print('LENDO A FRASE')
print('='*50)

#Entrada de dados
frase = str(input('Digite uma frase: '))

#Conversão de strings
fraseQuebrada = frase.split()
minusculo = frase.lower()
maiusculo = frase.upper()
quantidadeCaracteres = len(frase)
quantidadeLetras = len(fraseQuebrada[1])

#Saída
print(f'A frase "{frase}" em minusculo é: {minusculo}')
print(f'A frase "{frase}" maiusculo é: {maiusculo}')
print(f'A frase "{frase}" tem {quantidadeCaracteres} caracteres')
print(f'A segunda palavra da frase "{frase}" tem {quantidadeLetras} letras')

print('-'*50)
print()