# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 11:26:51 2016

@author: dmitry
"""

import math

def linspace(begin, end, n):
  """ Renvoie une liste de points espacés de manière régulière
      pour un intervalle donné.

 Paramètres
 ==========

 begin : borne inférieure de l'intervalle

 end : borne supérieure de l'intervalle

 n : nombre de points

 Sortie
 ======

 Renvoie la liste des points de discrétisation.
"""
  
  if end < begin:
      print ('*** linspace() Error: end must be greater than begin')
      return None
      
  h = (end - begin)/(n-1)
  return [begin + i*h for i in range(n)]

def spe_cos(w, m):
  cosw = math.cos(w)
  return math.copysign(abs(cosw)**m, cosw)

def spe_sin(w, m):
  sinw = math.sin(w)
  return math.copysign(abs(sinw)**m, sinw)


def superellipse(n=5, rx=1, ry=1, m=2):

  x = []
  y = []
  for theta in linspace(0., 2.*math.pi, n):
    x.append(rx*spe_cos(theta, 2./m))
    y.append(ry*spe_sin(theta, 2./m))
  return x, y
