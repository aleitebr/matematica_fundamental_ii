# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 04:27:06 2024
Última Modificação: 22 de Julho de 2024

@author: aleitebr

Script Name: poligonos_regulares_v3.py
Cácula o tamanho da aresta inscrito no cículo de raio RAIO com a lei dos cossenos
Desenha a Circunferência que circunscreve o polígono
"""
import turtle
import math

RAIO = 250

t = turtle.Pen()
t.pencolor('blue')
turtle.bgcolor('white')
t.speed(1)
posicao_inicial = t.pos()

n_arestas_poligono = 2
while (n_arestas_poligono < 3):
    n_arestas_poligono = int(input('Digite o número de arestas para o polígono (n >= 3)? '))
    if n_arestas_poligono < 3:
        print('Erro: Digite num número maior que 2.')

# inicializa lista de poligonos
n_arestas_poligono = [60, n_arestas_poligono]
angulo_interno = []
angulo_central = []
comprimento_aresta = []
apotema = []

for indice in range(2):
    # calculamos os valores do ângulo interno e central do polígono
    angulo_interno.append((n_arestas_poligono[indice] - 2) * 180 / n_arestas_poligono[indice])
    angulo_central.append( 360 / n_arestas_poligono[indice] )

    # quanto maior o número de arestas, menor o tamanho das arestas, para caber na tela 
    comprimento_aresta.append( math.sqrt(2*(RAIO**2) - 2*(RAIO**2)*math.cos(angulo_central[indice] * math.pi / 180)))

    # é necessário encontrar o comprimento do apótema para poder centralizá-lo
    apotema.append(( comprimento_aresta[indice] / 2 ) / math.tan( angulo_central[indice] / 2 * math.pi / 180 )) 

for indice in range(2):
    # levanta a caneta para não escrever enquanto se move primeiro vértice do polígono
    t.penup()
    t.goto(posicao_inicial)
    # move para a direita 90 graus
    t.right(90)
    t.forward( apotema[indice] )
    t.right(90)
    t.forward( comprimento_aresta[indice] / 2 )
    t.right(180)
    # baixa a caneta para desenhar o polígono
    t.pendown()

    for x in range( n_arestas_poligono[indice] ):
       t.forward( comprimento_aresta[indice] )
       t.left( 180 - angulo_interno[indice] ) # vira a esquerda o valor do ângulo externo

