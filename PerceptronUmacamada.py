#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 19:39:06 2019

@author: mtes
"""

import numpy as np

#Operador XOR
#entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
#saidas = np.array([0,1,1,0])

entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
saidas = np.array([0,0, 0,1])
pesos = np.array([0.0, 0.0])
taxadeAprendizagem = 0.1

#Calcula a Step function
def stepFunction(soma):
    if(soma >=1):
        return 1
    else:
        return 0

#Calcula a Função Soma
def calSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)

#Realiza o calculo do ajuste de peso
def ajustepeso():
    erroTotal = 1
    while(erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaPronta = calSaida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saidaPronta)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxadeAprendizagem * entradas[i][j] * erro)
                print('Peso novo:' + str(pesos[j]))
        print('Erros Detectados' + str(erroTotal))
            
ajustepeso()
print("Rede Neural pronta")
print(calSaida(entradas[0]))
print(calSaida(entradas[1]))
print(calSaida(entradas[2]))
print(calSaida(entradas[3]))
