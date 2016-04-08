# coding: utf8
"""
implémentation d'une superellipsoide
"""

import numpy as np

from ..utils import spe_cos, spe_sin
from .superellipse import Superellipse

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

    cloud_with_square: renvoie les points de la surface en projetant un cube.

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
        phi = np.linspace(-.5*np.pi, .5*np.pi, self.n)[:, np.newaxis]
        theta = np.linspace(-np.pi, np.pi, self.n)[np.newaxis, :]

        x = self.rx*spe_cos(phi, 2./self.m2)*spe_cos(theta, 2./self.m1)
        y = self.ry*spe_cos(phi, 2./self.m2)*spe_sin(theta, 2./self.m1)
        z = self.rz*spe_sin(phi, 2./self.m2)*np.ones(theta.shape)
        return x, y, z

    def cloud_with_square(self, n=10):
        """
        retourne les points à la surface de la superellipsoid
        en projetant un carré sur  deux superellipses et en 
        faisant leur produit sphérique.

        n : nombre de points de discrétisation sur un coté du carré

        """
        s1 = Superellipse(1, 1, self.m1)
        s2 = Superellipse(1, 1, self.m2)

        gx, gy = s1.cloud_with_square(n)
        hx, hy = s2.cloud_with_square(n)

        x = self.rx*gx[np.newaxis, :]*hx[:, np.newaxis]
        y = self.ry*gx[np.newaxis, :]*hy[:, np.newaxis]
        z = self.rz*gy[np.newaxis, :]*np.ones(hx.size)[:, np.newaxis]

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
        return 4*np.pi*self.rx**2
