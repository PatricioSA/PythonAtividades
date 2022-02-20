#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 28/10/2021
#Término: 28/10/2021
#Atividade003 - Exercício b

from datetime import date

import os


os.system('cls')

#Entrada de dados
anoAtual = date.today().year
anoNascimento = int(input('Digite seu ano de nascimento: '))

#operações
idade = anoAtual - anoNascimento

#Saída
print(f'Sua idade é: {idade} anos')