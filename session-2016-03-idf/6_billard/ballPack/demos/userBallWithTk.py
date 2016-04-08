#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
import time
import ballPack as bp
from math import sin, pi

# taille de la fenetre
width, height = 500, 400 
# délai de raffraichissement
delay = .05

# palette de couleur
color = bp.Color()

# création de la balle
balls = []

radius = 40
x, y = width/2, height/2
vx = vy = 1
balls.append(bp.UserBall(x, y, vx, vy, radius,
                         [0, width], [0, height]))

# initialisation de l'environnement graphique
root = Tk()

can = Canvas(root, width = width, height = height)
can.pack()

def movefunc(x, y, vx, vy, i, amplitude, freq, height):
    return x + vx, height/2 + amplitude*sin(freq*i*2*pi/height)

ind = 0
while 1:
    root.update() # force mise a jour du dessin
    time.sleep(delay)
    
    can.delete("all")

    for ball in balls:
        ball.move(movefunc, (ind, 100, 5, height))
        x, y = ball.coords
        radius = ball.radius
        can.create_oval(x - radius, y - radius, 
                        x + radius, y + radius, 
                        fill=ball.color)
        ind += 1
