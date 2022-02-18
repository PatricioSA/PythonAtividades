#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 07/12/2021
#Término: /12/2021

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*80)
print('')
print('='*80)

#Declaração
alunosNotas = {
    'Patrício': 9,
    'Igor': 8,
    'Abner': 8,
    'Calixto': 7.5
}

novosAlunos = {'Pedro': 7, 'Gustavo': 7}
alunosNotas.update(novosAlunos)
print(f'A lista de alunos são: {alunosNotas}')

apagar = str(input('Qual aluno deseja apagar?: ')).capitalize()
del(alunosNotas[apagar])

#Saída
print('Nome: \t\t\tNota:')
for chave, valor in alunosNotas.items():
    print(f'{chave}    \t\t{valor}')