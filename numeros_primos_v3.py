# -*- coding: utf-8 -*-
"""
Crivo de Erástoteles
Autor: Alexandre Cardoso Garcia Leite.
Data: 08/07/2024

Script: numeros_primos_v3.py
"""

lista_numeros_naturais = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                          21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
proximo_numero_primo = 2
num_primos_encontrados = 1

# Enquanto índice inicial for menor do que o tamanho da lista
while (num_primos_encontrados < len(lista_numeros_naturais)):
    i = num_primos_encontrados
    while (i < len(lista_numeros_naturais)):
        if lista_numeros_naturais[i] % proximo_numero_primo == 0:
            del lista_numeros_naturais[i]
            i = i - 1
        i = i + 1    
    try:
        proximo_numero_primo = lista_numeros_naturais[num_primos_encontrados]
    except IndexError:
        pass
    num_primos_encontrados = num_primos_encontrados + 1
        
lista_numeros_primos = lista_numeros_naturais
print(lista_numeros_primos)

