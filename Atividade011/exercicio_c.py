#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 06/02/2022
#Término: /02/2022

import os


#Limpar terminal
os.system('cls')

#Título
print('-'*80)
print('Cadastro de Alunos')
print('='*80)

listaAluno = []
alunos = {}

for c in range(0,2):

    #Entrada de dados
    alunos['Nome'] = str(input('Digite o nome: '))
    alunos['Matrícula'] = int(input('Entre com a matrícula: '))
    alunos['Data de nascimento'] = int(input('Digite a data de nascimento: '))

    listaAluno.append(alunos.copy)

print()
verificacao = str(input('Qual nome deseja verificar?: '))

#Função para verificar se o aluno está cadastrado
def verificar_aluno():
    while (True):
        if verificacao in listaAluno:
            print(f'{verificacao} está cadastrado')
        else:
            print('Não está cadastrado')
            print()
            print('o que deseja? ')
            print('1 = verificar outro aluno, 2 = cadastrar aluno')
            escolha = int(input(': '))
            if escolha == 1:
                continue
            else:
                break

#Invocando a função
verificar_aluno()