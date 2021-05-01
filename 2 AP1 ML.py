# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 16:28:28 2021

@author: danie
"""

""" Fazer um programa para calcular atualizar os lançamentos contábeis diários de uma empresa. 
O sistema deverá ler os lançamentos diários, compostos pelo valor do lançamento e o tipo de lançamento ('D' - Débito ou 'C' - Crédito). 
O programa deve calcular o total de créditos e débitos feito pela empresa no mês. Sabe-se que a cada mês são realizados 44 lançamentos. Ao final do programa, exibir os totais de Crédito e Débito, bem como informar se a empresa teve lucro, prejuízo ou os débitos e créditos foram iguais, informando também essa diferença.
"""
valor = float(input('Insira o valor da lançamento:'))
tipo = input('Qual o tipo da conta? D para débito e C para crédito.')


totD = 0
totC = 0

if tipo != 'C' or tipo != 'D':
    print('Valor inválido!')
else:

    for i in range(44):
        if tipo == 'C':
            totD = totD + valor
        else:
            totC = totC + valor
print('O total de débito é de : R$', totD)
print('O total de crédito é de: R$', totC)

balanco = totD-totC
if balanco < 0:
    print('Houve um prejuízo de: R$', balanco)
elif balanco==0:
    print('As contas débito e crédito são iguais.')
else:
    print('Houve um lucro de: R$', balanco)
    
    


        
    
    
    