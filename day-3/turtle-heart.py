"""
Desenhando coração com python
"""

# import turtle
import turtle
import time

# caneta
pen = turtle.Turtle()

# funcao para fazer curvas
def curve():
    # loop
    for i in range(200):
        pen.right(1)
        pen.forward(1)

# funcao desenhar coracao
def heart():
    time.sleep(2)
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()
    
# coracao
heart()

# close pen
pen.ht()

# fechar programa
input("Pressione <enter> para encerrar!")