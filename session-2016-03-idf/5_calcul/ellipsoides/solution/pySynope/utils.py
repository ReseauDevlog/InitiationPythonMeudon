# coding: utf8
"""
Fonctions utilisées dans la création des

- superellipses
- superellipsoides

"""

import numpy as np

def spe_cos(theta, m):
    """
    calcule sign(cos(theta))|cos(theta)|^m
    """
    cos_t = np.cos(theta)
    return np.sign(cos_t)*np.abs(cos_t)**m

def spe_sin(theta, m):

    """
    calcule sign(sin(theta))|sin(theta)|^m
    """
    sin_t = np.sin(theta)
    return np.sign(sin_t)*np.abs(sin_t)**m
    