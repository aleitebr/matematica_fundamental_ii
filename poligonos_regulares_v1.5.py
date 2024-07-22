# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 04:27:06 2024
Última Modificação: 22 de Julho de 2024

@author: aleitebr

Script Name: poligonos_regulares_v1.5.py
"""
import turtle
import math

t = turtle.Pen()
t.pencolor('blue')
turtle.bgcolor('black')

n_arestas_poligono = 2
while (n_arestas_poligono < 3):
    n_arestas_poligono = int(input('Digite o número de arestas para o polígono (n >= 3)? '))
    if n_arestas_poligono < 3:
        print('Erro: Digite num número maior que 2.')

angulo_interno = (n_arestas_poligono - 2) * 180 / n_arestas_poligono
angulo_central = 360 / n_arestas_poligono

# quanto maior o número de arestas, menor o tamanho das arestas, para caber na tela
comprimento_aresta = int(500 / n_arestas_poligono)

# é necessário encontrar o comprimento do apótema para poder centralizá-lo
apotema = ( comprimento_aresta / 2 ) / math.tan( angulo_central / 2 * math.pi / 180 ) 

# move para a direita 90 graus
t.right(90)
# levanta a caneta para não escrever enquanto se move primeiro vértice do polígono
#t.penup()
t.forward( apotema )
t.right(90)
t.forward( comprimento_aresta / 2 )
t.right(180)
# baixa a caneta para desenhar o polígono
#t.pendown()

for x in range( n_arestas_poligono ):
    t.forward( comprimento_aresta )
    t.left( 180 - angulo_interno ) # vira a esquerda o valor do ângulo externo

