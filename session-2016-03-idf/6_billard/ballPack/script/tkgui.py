#! /usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from random import randint
import tempfile
from ballPack import *

class BallApp(object):
    def __init__(self, parent, width=800, heigth=600, delay=10):
        self.parent = parent
        self.width = width
        self.height = height
        self.delay = delay
        self.start = False

        self.filename = tempfile.NamedTemporaryFile()

        self.createWindow()

        self.parent.bind("<Key>", self.saveAndLoadState)

        self.nbbb.set("0")
        self.nbgb.set("0")

    def createWindow(self):
        root = self.parent
        self.can = Canvas(root, width = width, height = height, background="white")
        txt1 = Label(root, text ='Boncing ball :')
        txt2 = Label(root, text ='Gravity Ball :')
        self.nbbb = StringVar()
        edit1 = Entry(root, textvariable=self.nbbb)
        self.nbgb = StringVar()
        edit2 = Entry(root, textvariable=self.nbgb)
        self.button = Button(root, text ='Start', command=self.startButton)
        
        self.can.grid(row = 0, column = 0, columnspan=2, padx = 10, pady = 25)
        txt1.grid(row = 1)
        txt2.grid(row = 2)
        edit1.grid(row = 1, column = 1)
        edit2.grid(row = 2, column = 1)
        self.button.grid(row=3, columnspan = 2)

        txt3 = Label(root, text ='type "s" to save state, "l" to load state, "p" for pause')
        txt3.grid(row = 4, columnspan=2)

    def initBalls(self, method, nb):
        balls = []

        for i in range(nb):
            radius = randint(5, 10)
            x = randint(radius, width - radius - 1)
            y = randint(radius, height - radius - 1)
            vx = randint(0, 10)
            vy = randint(0, 10)
            c = color.getRandomColor()
            balls.append(method(x, y, vx, vy, radius,
                                 [0, width], [0, height],
                                 c))
        return balls

    def startButton(self):
        self.start = not self.start
        self.button.focus()

        if self.start:
            self.button["text"] = "Stop"
            self.balls = self.initBalls(BouncingBall, int(self.nbbb.get()))
            self.balls += self.initBalls(GravityBall, int(self.nbgb.get()))
            self.move()
        else:
            self.button["text"] = "Start"

    def move(self):
        # on efface toutes les balles
        self.can.delete("all")
    
        # on déplace les balles puis on les affiche
        for ball in self.balls:
            ball.move()
            x, y = ball.coords
            radius = ball.radius
            self.can.create_oval(x - radius, y - radius, 
                                 x + radius, y + radius, 
                                 fill=ball.color)
        if self.start:
            self.parent.after(self.delay, self.move)

    def saveAndLoadState(self, event):
        if event.char == 's' and self.start:
            print("save in " + self.filename.name)
            saveBalls(self.balls, self.filename.name)
        if event.char == 'l' and self.start:
            print("load from " + self.filename.name)
            self.balls = readBalls(self.filename.name)
        if event.char == 'p':
            self.start = not self.start
            if self.start:
                self.move()


if __name__ == '__main__':
    # taille de la fenetre
    width, height = 500, 400 
    # délai de raffraichissement
    delay = 10

    # palette de couleur
    color = Color()

    # initialisation de l'environnement graphique
    root = Tk()
    root.title("BallPack application")
    app = BallApp(root)
        
    root.mainloop()


