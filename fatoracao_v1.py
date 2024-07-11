# -*- coding: utf-8 -*-
"""
Fatoração de um número natural em seus números primos.
Autor: Alexandre Cardoso Garcia Leite.
Criação: 08/07/2024
Última Atualização: 08/07/2024

"""

numero = int(input("Digite o número que você quer fatorar?"))

"""
Antes obteremos os números primos entre 2 e 1.000, aplicando o algoritmo de Erastotenes
"""
lista_numeros_naturais = []

# Cria uma lista com os números naturais começando pelo número primo 2 
for i in range(2,1000):
    lista_numeros_naturais.append(i)
    
proximo_numero_primo = 2
num_primos_encontrados = 1

# Enquanto a lista de numeros primos for menor do que a lista de do restante dos numeros naturais
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
        
l_num_primos = lista_numeros_naturais

"""
Com a lista de números primos em mãos, faremos em seguida a fatoração.
"""

numero = 2**8 * 3**2

num_fatorado = {}

n_num_primo = 0

while (numero != 1):
    while (numero !=1 and numero % l_num_primos[n_num_primo] == 0):
        if l_num_primos[n_num_primo] not in num_fatorado:
            num_fatorado[l_num_primos[n_num_primo]] = 1
        else:
            num_fatorado[l_num_primos[n_num_primo]] = num_fatorado[l_num_primos[n_num_primo]] + 1
        numero = int(numero / l_num_primos[n_num_primo]) 
    n_num_primo = n_num_primo + 1
    
print(num_fatorado)
        


