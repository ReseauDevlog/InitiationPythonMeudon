# coding: utf8
"""
implémentation d'une fonction linspace
"""
from six.moves import range

def linspace(begin, end, npoints):
    """
    Renvoie une liste de points espacés de manière régulière
    pour un intervalle donné.

    Paramètres
    ==========

    begin : borne inférieure de l'intervalle

    end : borne supérieure de l'intervalle

    npoints : nombre de points

    Sortie
    ======

    Renvoie la liste des points de discrétisation.

    """
    step = (end - begin)/(npoints-1)
    return [begin + i*step for i in range(npoints)]
