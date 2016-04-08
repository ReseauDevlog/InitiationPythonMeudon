# -*- coding: utf-8 -*-

class Ball:
    def __init__(self, x, y, vx=1, vy=1, radius=20, xdomain=[0, 800], ydomain=[0, 600], color='green'):
        """
        Initialisation de la classe Balle

        Paramètres
        ----------

            x       : coordonnée du centre de la balle suivant x
            y       : coordonnée du centre de la balle suivant y
            vx      : vitesse de la balle suivant x
                      par défaut: 1
            vy      : vitesse de la balle suivant y
                      par défaut: 1
            radius  : rayon de la balle
                      par défaut: 20
            xdomain : domaine de la balle suivant x
                      par défaut: [0, 800]
            ydomain : domaine de la balle suivant y
                      par défaut: [0, 600]
            color   : couleur de la balle
                      par défaut: "green"
        
        """ 
        self.coords = [x, y]
        self.radius = radius
        self.v = [vx, vy]
        self.color = color
        self.domain = [xdomain, ydomain]

    def move(self):
        """
        Déplacement de la balle

        """
        pass

    def checkVelocity(self):
        """
        Regarde si la balle ne sort pas du domaine. 

        Si elle sort, on inverse les vitesses et on remet la balle
        sur le bord.

        La fonction renvoie:
            - vrai si on a touché
            - faux sinon

        """
        touch = False
        for i in range(2):
            if self.coords[i] < self.domain[i][0] + self.radius:
                self.v[i] *= -1
                self.coords[i] = self.domain[i][0] + self.radius 
                touch = True
            if self.coords[i] > self.domain[i][1] - self.radius:
                self.v[i] *= -1
                self.coords[i] = self.domain[i][1] - self.radius
                touch = True
        return touch
        

    def __str__(self):
        s = 'Ball:\n'
        s += '\t coord    : {0}\n'.format(self.coords)
        s += '\t velocity : {0}\n'.format(self.v)
        s += '\t radius   : {0}\n'.format(self.radius)
        s += '\t color    : {0}\n'.format(self.color)
        s += '\t domain   : {0}\n'.format(self.domain)
        return s

    def __repr__(self):
        return self.__str__()

class BouncingBall(Ball):
    def move(self):
        """
        On déplace la balle en la faisant rebondir.
        """

        self.coords[0] += self.v[0]
        self.coords[1] += self.v[1]
        self.checkVelocity()

class GravityBall(Ball):
    def move(self):
        """
        On déplace la balle avec une vitesse suivant y liée
        à la gravité.

        A chaque fois qu'elle touche un bord, elle est amortie.
        """
        deltaT = .1
        g = 9.81
        amort = .9

        self.v[1] -= g*deltaT;
        self.coords[0] += self.v[0]*deltaT;
        self.coords[1] -= self.v[1]*deltaT;

        if self.checkVelocity():
            self.v[0] *= amort
            self.v[1] *= amort

class UserBall(Ball):
    def move(self, movefunc, movefunc_args=()):
        self.coords[0], self.coords[1] = movefunc(self.coords[0], self.coords[1], self.v[0], self.v[1], *movefunc_args)
        self.checkVelocity()

if __name__ == '__main__':
    b = BouncingBall(1, 1)    
    for i in range(5):
        print(b)
        b.move()
