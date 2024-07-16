# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 04:27:06 2024

@author: aleitebr

Script Name: PoligonosRegulares_v1.py
"""
import turtle
import math

t = turtle.Pen()
t.pencolor('blue')
turtle.bgcolor('black')

lados_poligono = 2
while (lados_poligono < 3):
    lados_poligono = int(input('Digite o número de lados para o polígono (n >= 3)? '))
    if lados_poligono < 3:
        print('Erro: Digite num número maior que 2.')

angulo = (lados_poligono - 2) * 180 / lados_poligono
angulo_central = 360 / lados_poligono

# quanto maior o número de lados, menor o número das arestas, para caber na tela
comp_lado_oposto = int(500 / lados_poligono)

# é necessário dividir o polígono em triângulos, para poder centralizá-lo
comp_lado_adjacente = ( comp_lado_oposto / 2 ) / math.tan( angulo_central / 2 * math.pi / 180 ) 

# move para a direita 90 graus
t.right(90)
# levanta a caneta para não escrever enquanto se move primeiro vértice do polígono
t.penup()
t.forward( comp_lado_adjacente )
t.right(90)
t.forward( comp_lado_oposto / 2 )
t.right(180)
# baixa a caneta para desenhar o polígono
t.pendown()

for x in range( lados_poligono ):
    t.forward( comp_lado_oposto )
    t.left( 180 - angulo )

