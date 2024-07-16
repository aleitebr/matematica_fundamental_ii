# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 04:27:06 2024

@author: aleitebr

Script Name: PoligonosRegulares_v1.py
"""
import turtle
t = turtle.Pen()
t.pencolor('blue')
turtle.bgcolor('black')

lados_poligono = 2
while (lados_poligono < 3):
    lados_poligono = int(input('Digite o número de lados para o polígono (n >= 3)? '))
    if lados_poligono < 3:
        print('Erro: Digite num número maior que 2.')

angulo = (lados_poligono - 2) * 180 / lados_poligono

comp_lado = int(1000 / lados_poligono)

for x in range(lados_poligono):
    t.forward(comp_lado)
    t.left(180 - angulo)
