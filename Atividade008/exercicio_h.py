#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 26/11/2021
#Término: /11/2021
#Atividade008 - exercicio h
# Faça um programa que leia um número indeterminado de notas (pressione ‘s’ ou ‘0’ para sair). 
# Após esta entrada de dados, faça o seguinte: 
# • Mostre a quantidade de notas que foram lidas.
# • Exiba todas as notas na ordem em que foram informadas.
# • Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo do outra.
# • Calcule e mostre a soma das notas.
# • Calcule e mostre a média das notas.

#Limpar o terminal
import os


os.system('cls')

#Declarações
listaNotas = []
soma = 0
media = 0
quantidade = 0

while (True):
    print('='*70)

    #Entrada de dados
    nota = input('Digite a nota: ').lower()
    
    if(nota == 's'):               
        break
    
    # Validação
    else:
        if ((not(nota.isnumeric()))):
            print()
            print(f'Entrada Inválida, digite novamente...')
            print()
        else:
             nota = float(nota)
             listaNotas.append(nota)
             soma += nota
             quantidade += 1
             media = soma / quantidade

#Funções de listas
listaInversa = sorted(listaNotas, reverse=True)

#Saída
print()
print(f'A quantidade de notas lidas foi: {quantidade}')
print(f'As notas na ordem informada são: {listaNotas}')
print(f'As notas na ordem iversa são: {listaInversa}')
print(f'A soma das notas é: {soma}')
print(f'A média das notas é: {media:.2f}')

print('-'*60)
print('Fim do programa!')
print()