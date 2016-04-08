# coding: utf8
"""
implémentation d'une superellipse
"""
import numpy as np

from ..utils import spe_cos, spe_sin

class Superellipse(object):
    """
    définit une superellipse.

    x = rx c(theta, 2/m)
    y = ry s(theta, 2/m)

    où 

    c(theta, m) = sign(cos(theta))|cos(theta)|**m
    s(theta, m) = sign(sin(theta))|sin(theta)|**m
    
    Paramètres
    ==========

    n : nombre de points de discrétisation en theta

    rx : rayon suivant x

    ry : rayon suivant y

    m : puissance dans l'expression de la superellipse.

    Attributs
    =========
    rx : rayon suivant x

    ry : rayon suivant y

    m : puissance dans l'expression de la superellipse.

    Méthodes
    ========

    cloud: renvoie les points de la surface.

    cloud_with_square: renvoie les points de la surface en projetant un carré.
    
    area: renvoie l'aire.

    """

    def __init__(self, rx, ry, m):
        self.rx = rx
        self.ry = ry
        self.m = m

    def cloud(self, n=10):
        """
        retourne les points à la surface de la superellipse

        Paramètre
        =========

        n : nombre de points de discrétisation

        """
        theta = np.linspace(0., 2.*np.pi, n)
        return self.rx*spe_cos(theta, 2./self.m), \
            self.ry*spe_sin(theta, 2./self.m)

    def cloud_with_square(self, n=10):
        """
        retourne les points à la surface de la superellipse
        en projetant un carré sur celle-ci

        Paramètre
        =========

        n : nombre de points de discrétisation sur un coté du carré

        """
        x = np.concatenate((np.linspace(-1, 1., n), 
            np.ones(n-2), np.linspace(1, -1., n),
            -np.ones(n-2)))
        y = np.concatenate((-np.ones(n-1), 
            np.linspace(-1, 1., n), np.ones(n-2), 
            np.linspace(1, -1., n-1, endpoint=False)))
        return x*self.rx*(1. - .5*np.abs(y)**self.m)**(1./self.m),  y*self.ry*(1. - .5*np.abs(x)**self.m)**(1./self.m)

    @property
    def area(self):
        """
        retourne l'aire de la superellipse
        """
        r = 1./self.m
        return 4**(1-r)*self.rx*self.ry*math.sqrt(np.pi)*math.gamma(1+r)/math.gamma(.5+r)

class Circle(Superellipse):
    """
    définit un cercle à partir d'une superellipse
    """
    def __init__(self, r):
        super(Circle, self).__init__(r, r, 2)

    @property
    def perimeter(self):
        """
        retourne le préimètre d'un cercle
        """
        return 2*np.pi*self.rx