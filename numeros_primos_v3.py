# -*- coding: utf-8 -*-
"""
Crivo de Erástoteles
Autor: Alexandre Cardoso Garcia Leite.
Data: 08/07/2024

Script: numeros_primos_v3.py
"""

lista_numeros_naturais = []

# Cria uma lista com os números naturais começando pelo número primo 2 
for i in range(2,1000):
    lista_numeros_naturais.append(i)
    
proximo_numero_primo = 2
num_primos_encontrados = 1

# Enquanto número de números primos for menor do que o tamanho da lista
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

