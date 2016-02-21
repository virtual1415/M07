# Patricio Vidal
# -*- coding: utf-8 -*-

import random

def creacioMatriuAleatoria(n):
    matriu = []
    for i in range(n):
        matriu.append([])
        for j in range(n):
            matriu[i].append(random.randint(0,15))
    return matriu

def sumaMatrius(matriu1, matriu2, n):
    matriuRes = []
    for i in range(n):
        matriuRes.append([])
        for j in range(n):
            matriuRes[i].append(matriu1[i][j] + matriu2[i][j])
    return matriuRes

def multiplicaMatrius(matriu1, matriu2, n):
    matriuRes = []
    for i in range(n):
        matriuRes.append([])
        for j in range(n):
            matriuRes[i].append(0)
            for k in range(n):
                matriuRes[i][j] += (matriu1[i][k] * matriu2[k][j])
    return matriuRes