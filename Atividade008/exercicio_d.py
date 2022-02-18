#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 26/11/2021
#Término: /11/2021
#Atividade008 - exercicio d
#Faça um programa que preencha uma lista com as notas de 4 alunos, depois imprima a média.

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*70)
print('Média das notas')
print('='*70)

#Criando uma lista
listaNota = []
media = 0


for c in range (0, 4):

    #Entrada de dados
    nota = float(input(f'Digite a nota: '))

    #Validação
    while (nota < 0):
        print(f'Nota Inválida')
        nota = float(input(f'Digite a nota novamente: '))
    else:
        #Adicionando nota na lista
        listaNota.append(nota)

        #Cálculo da média
        media += nota / 4

#Saída
print()
print(f'As notas são: {listaNota}')  
print(f'A média das notas é: {media}')
print()