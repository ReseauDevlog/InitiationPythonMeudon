# coding: utf8
"""
Implémentation des quaternions
"""
from __future__ import print_function
import math

class Quaternion(object):
    """
    classe définissant un quaternion

    q = w + x i + y j + z k

    Paramètres
    ==========

    - x : double
    - y : double
    - z : double
    - w : double

    """
    def __init__(self, w=0, x=0, y=0, z=0):
        self.coords = [x, y, z]
        self.w = w

    def set_angle(self, angle, axe=[0, 0, 1]):
        """
        modifie le quaternion en fonction de l'angle et de l'axe
        """
        c = math.sin(angle/2)
        self.coords = [c*a for a in axe]
        self.w = math.cos(angle/2)

    def rotate(self, pos):
        """
        retourne la position tournée par le quaternion
        """
        qpos = Quaternion(0, *pos)
        return (self*qpos*self.conjugate()).coords

    @property
    def x(self):
        return self.coords[0]

    @x.setter
    def x(self, value):
        self.coords[0] = value

    @property
    def y(self):
        return self.coords[1]

    @y.setter
    def y(self, value):
        self.coords[1] = value

    @property
    def z(self):
        return self.coords[2]

    @z.setter
    def z(self, value):
        self.coords[2] = value

    def __add__(self, q):
        return Quaternion(self.w + q.w,
                          self.x + q.x,
                          self.y + q.y,
                          self.z + q.z
                          )

    def __sub__(self, q):
        return Quaternion(self.w - q.w,
                          self.x - q.x,
                          self.y - q.y,
                          self.z - q.z
                          )

    def __mul__(self, q):
        return Quaternion(self.w*q.w - self.x*q.x - self.y*q.y - self.z*q.z,
                          self.w*q.x + self.x*q.w + self.y*q.z - self.z*q.y,
                          self.w*q.y - self.x*q.z + self.y*q.w + self.z*q.x,
                          self.w*q.z + self.x*q.y - self.y*q.x + self.z*q.w)

    def conjugate(self):
        """
        retourne le conjugué du quaternion
        """
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def normalize(self):
        """
        normalise le quaternion
        """
        norm = abs(self)
        if norm == 0.:
            norm = 1.
        self.w /= norm
        self.x /= norm
        self.y /= norm
        self.z /= norm

    def __abs__(self):
        return math.sqrt(self.w*self.w +
                         self.x*self.x +
                         self.y*self.y +
                         self.z*self.z)

    def __str__(self):
        return '{} {:+} i {:+} j {:+} k'.format(self.w, *self.coords)

    def __repr__(self):
        return self.__str__()

if __name__ == '__main__':
    q = Quaternion()
    print(q)

    q.set_angle(math.pi/4)
    q.normalize()
    print(q)

    print(q.rotate([1, 0, 0]))
