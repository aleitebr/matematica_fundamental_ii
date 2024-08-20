# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 04:27:06 2024
Última Atualização: 19/08/2024

@author: aleitebr

Script Name: PoligonosRegulares_v2.py
"""
# Importa bibliotecas necessárias para a execução do algoritmo
import turtle
import math

# Define o valor do raio da circunferência
RAIO = 250 

# Atribui ao identificador "t" a expressão turtle.Pen()
t = turtle.Pen()

t.speed(1) # Seta a velocidade que o desenho vai ser executado
t.pencolor('blue') # Define a cor da caneta para 'azul'
turtle.bgcolor('white') # Define o fundo da tela para branco

lados_poligono = 2 # não existe polígonos com menos de 3 lados
while (lados_poligono < 3): # enquanto o usuári não digitar um valor n >= 3, continua perguntando por um valor válido
    # pergunta ao usuário o número de lados do polígono que ele quer desenhar
    lados_poligono = int(input('Digite o número de lados para o polígono (n >= 3)? '))
    
    if lados_poligono < 3: # se lados do poligno for menor que 3, envia
                           # uma mensagem para o usuário e refaz a pergunta
        print('Erro: Digite num número maior que 2.')

# Calcula o ângulo interno do polígono reguar, note que a soma dos ângulos internos podem ser divididas pelo numero de lados_poligono
# por cause que estamos tratando de polígonos regulares
angulo_interno = (lados_poligono - 2) * 180 / lados_poligono

# chamamos de angulo central o ângulo que a cincunferência faz com cada lado
# do polígono
angulo_central = 360 / lados_poligono

# aplica a lei dos cossenos para calcular o comp_lado_oposto
comp_lado_poligono = math.sqrt(int(2*RAIO**2 - 2*RAIO**2*math.cos(angulo_central / 180 * math.pi)))

# para se obter o apótema é necessário dividir o polígono em triângulos e
# calcular a altura
apotema = ( comp_lado_poligono / 2 ) / math.tan( angulo_central / 2 / 180 * math.pi) 

# o módulo "turtle" incia com uma seta na posição central da tela indicando para a direita
t.right(90) # move a direita 90º para a direita
#t.penup() # levanta a caneta, mas como no desenho queremos ver o apótema desenhando
            # deixamos a caneta desenhar normalmente
t.pencolor('red')
t.forward( apotema ) # desenha apótema
t.right(90) # gira novamente 90º para a direta
t.pencolor('blue') # retorna a cor azul para desenhar o polígono
t.forward( comp_lado_poligono / 2 )
t.right(180) # move a seta 180º
# baixa a caneta para desenhar o polígono
#t.pendown()

# enquato x estiver entre [0, número lados poligono] desenha as arestas
for x in range( lados_poligono ):
    t.forward( comp_lado_poligono )
    t.left( 180 - angulo_interno ) # move para a esquerda a caneta
                                   # observe que giramos o ângulo externo do polígno,
                                   # não o ângulo interno
                 

