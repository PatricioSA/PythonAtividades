#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 04/11/2021
#Término: 04/11/2021
#Atividade004 - Exercício d

#Limpando terminal
import os
os.system('cls')

print('-'*30)
print('CÁLCULO DE AUMENTO DE SALÁRIO ')
print('-'*30)

#Declarações e Entrada de dados
salario = float(input('Digite o salário: '))
cinco = (5 / 100 * salario) + salario
dez = (10 / 100 * salario) + salario

#Condicionais
if (salario <= 0):
    print('Valor Inválido: o salário não pode ser menor ou igual a 0')
elif (salario > 1500):
    print(f'O novo salário é de: R${cinco:.2f}')
elif (salario < 1000):
    print(f'O novo salário é de: R${dez:.2f}')

print()
print('Fim do Progamra! ')