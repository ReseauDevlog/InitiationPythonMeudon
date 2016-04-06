# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 11:25:56 2016

@author: dmitry
"""

import math

def spe_cos(w, m):
  cosw = math.cos(w)
  return math.copysign(abs(cosw)**m, cosw)

def spe_sin(w, m):
  sinw = math.sin(w)
  return math.copysign(abs(sinw)**m, sinw)
  
  