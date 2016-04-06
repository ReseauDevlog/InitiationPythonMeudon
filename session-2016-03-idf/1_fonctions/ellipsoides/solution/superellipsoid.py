# coding: utf8

from __future__ import print_function
from six.moves import range
import math


# """
# Renvoie une liste de points espacés de manière régulière
# pour un intervalle donné.
#
# Paramètres
# ==========
#
# begin : borne inférieure de l'intervalle
#
# end : borne supérieure de l'intervalle
#
# n : nombre de points
#
# Sortie
# ======
#
# Renvoie la liste des points de discrétisation.
#
# """

def linspace(begin, end, n):
  h = (end - begin)/(n-1)
  return [begin + i*h for i in range(n)]

def spe_cos(w, m):
  cosw = math.cos(w)
  return math.copysign(abs(cosw)**m, cosw)

def spe_sin(w, m):
  sinw = math.sin(w)
  return math.copysign(abs(sinw)**m, sinw)


# """
# Renvoie les coordonnées de la superellipse.
#
# x = rx c(theta, 2/m)
# y = ry s(theta, 2/m)
#
# où 
#
# c(theta, m) = sign(cos(theta))|cos(theta)|**m
# s(theta, m) = sign(sin(theta))|sin(theta)|**m
#
# Paramètres
# ==========
#
# n : nombre de points de discrétisation en theta
#
# rx : rayon suivant x
#
# ry : rayon suivant y
#
# m : puissance dans l'expression de la superellipse.
#
# Sortie
# ======
#
# les coordonnées de la superellipse.
#
# """

def superellipse(n, rx, ry, m):
  x = []
  y = []
  for theta in linspace(0., 2.*math.pi, n):
    x.append(rx*spe_cos(theta, 2./m))
    y.append(ry*spe_sin(theta, 2./m))
  return x, y


# """
# Renvoie les coordonnées de la superellipsoid.
#
# x = rx c(theta, 2/m1) c(phi, 2/m2)
# y = ry s(theta, 2/m1) c(phi, 2/m2)
# y = rz s(phi, 2/m2)
#
# où
# c(theta, m) = sign(cos(theta))|cos(theta)|**m
# s(theta, m) = sign(sin(theta))|sin(theta)|**m
#
# Paramètres
# ==========
#
# n : nombre de points de discrétisation en theta et en phi
#
# rx : rayon suivant x
#
# ry : rayon suivant y
#
# rz : rayon suivant z
#
# m : puissance dans l'expression de la superellipse.
#
# Sortie
# ======
#
# les coordonnées de la superellipse.
#
# """

def superellipsoid(n, rx, ry, rz, m1, m2):
  x = []
  y = []
  z = []
  for theta in linspace(-math.pi, math.pi, n):
    x.append([])
    y.append([])
    z.append([])
    for phi in linspace(-.5*math.pi, .5*math.pi, n):
      x[-1].append(rx*spe_cos(phi, 2./m2)*spe_cos(theta, 2./m1))
      y[-1].append(ry*spe_cos(phi, 2./m2)*spe_sin(theta, 2./m1))
      z[-1].append(rz*spe_sin(phi, 2./m2))
  return x, y, z


# """
# utility
# """

def myformat(values):
    fe = ['{:+.1f}']*len(values)
    fg = '('+', '.join(fe)+')'
    return fg.format(*values)

def myformat2d(values):
    temp =  []
    for v in values:
        temp.append(myformat(v))
    fe = ['{}']*len(temp)
    fg = '('+', '.join(fe)+')'
    return fg.format(*temp)


# """
# demonstration code
# """

x, y = superellipse(5, 1, 1, 2)
print("superellipse(5, 1, 1, 2)")
print(myformat(x))
print(myformat(y))

x, y, z = superellipsoid(4, 1, 1, 1, 2, 2)
print("superellipsoid(4, 1, 1, 1, 2, 2)")
print(myformat2d(x))
print(myformat2d(y))
print(myformat2d(z))
