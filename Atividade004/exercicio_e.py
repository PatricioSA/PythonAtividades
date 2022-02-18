#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 04/11/2021
#Término: 05/11/2021
#Atividade004 - Exercício e

#Limpando terminal
import os
os.system('cls')

print('-'*30)
print('CÁLCULO DE PASSAGEM ')
print('-'*30)

#Entrada de dados e declarações
distancia = float(input('Digite a distância da viagem em KM: '))
ateDuzentos = 0.70 * distancia
acimaDuzentos = 0.40 * distancia

#Condicionais
if (distancia > 0 and distancia <= 200):
    print(f'A passagem custa R${ateDuzentos:.2f}')
elif (distancia > 200):
    print(f'A passagem custa R${acimaDuzentos:.2f}')
else:
    print('Inválido')

print()
print('Fim do Programa! ')