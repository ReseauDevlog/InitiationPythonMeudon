# coding: utf8
"""
implémentation d'une superellipsoide
"""

import math

from ..linspace import linspace
from ..utils import spe_cos, spe_sin

def beta_func(r, t):
    """
    retourne la fonction beta.
    """
    return math.gamma(r)*math.gamma(t)/math.gamma(r+t)

class Superellipsoid(object):
    """
    Définit une superellipsoid.

    x = rx c(theta, 2/m1) c(phi, 2/m2)
    y = ry s(theta, 2/m1) c(phi, 2/m2)
    y = rz s(phi, 2/m2)

    où
    c(theta, m) = sign(cos(theta))|cos(theta)|**m
    s(theta, m) = sign(sin(theta))|sin(theta)|**m

    Paramètres
    ==========

    rx : rayon suivant x

    ry : rayon suivant y

    rz : rayon suivant z

    m : puissance dans l'expression de la superellipse.

    Attributs
    =========

    n : nombre de points de discrétisation en theta et en phi

    rx : rayon suivant x

    ry : rayon suivant y

    rz : rayon suivant z

    m : puissance dans l'expression de la superellipse.

    Méthodes
    ========

    cloud : renvoie le nuage de points de la surface.

    volume : renvoie le volume de la superellipsoide.
    """
    def __init__(self, rx, ry, rz, m1, m2):
        self.rx = rx
        self.ry = ry
        self.rz = rz
        self.m1 = m1
        self.m2 = m2

    def cloud(self, n=10):
        """
        retourne les points à la surface de la superellipsoide.

        Paramètre
        =========

        n : nombre de points de discrétisation en theta et en phi

        """
        phi_list = linspace(-.5*math.pi, .5*math.pi, n)
        theta_list = linspace(-math.pi, math.pi, n)

        x = []
        y = []
        z = []
        for theta in theta_list:
            x.append([])
            y.append([])
            z.append([])
            for phi in phi_list:
                x[-1].append(self.rx*spe_cos(phi, 2./self.m2)
                             *spe_cos(theta, 2./self.m1))
                y[-1].append(self.ry*spe_cos(phi, 2./self.m2)
                             *spe_sin(theta, 2./self.m1))
                z[-1].append(self.rz*spe_sin(phi, 2./self.m2))
        return x, y, z

    @property
    def volume(self):
        """
        retourne le volume de la superellipsoide.
        """
        r = 1./self.m1
        t = 1./self.m2
        return 8./3.*self.rx*self.ry*self.rz*r*t*beta_func(r, r)*beta_func(2*t, t)

class Sphere(Superellipsoid):
    """
    Définit une sphère à partir d'une superellipsoide.
    """
    def __init__(self, r):
        super(Sphere, self).__init__(r, r, r, 2, 2)

    @property
    def area(self):
        """
        retourne l'aire de la surface d'une sphère
        """
        return 4*math.pi*self.rx**2
