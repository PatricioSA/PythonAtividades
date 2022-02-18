#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 06/02/2022
#Término: /02/2022

#Limpar o terminal
import os


os.system('cls')

#Criando uma função
def cadastrar():
    alunos = {}
    lista = []

    for c in range(2):
        alunos['Nome'] = str(input('nome do aluno: '))
        alunos['Matrícula'] = int(input('Matrícula do aluno: '))
        alunos['Nascimento'] = str(input('Data de nascimento: '))

        lista.append(alunos.copy())

    os.system('cls')
    print('-'*70)
    print('Alunos Cadastrados')
    print('='*70)

    for aluno in lista:  #para cada elemento na minha lista
        for chave, valor in aluno.items():   #para cada chave e valor do aluno
            print(f'{chave} : {valor}', end=' ' + '\n')
        print('-'*80)

#Programa principal
print('-'*70)
print('Cadastro de Alunos')
print('='*70)
cadastrar()