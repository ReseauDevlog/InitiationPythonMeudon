# -*- coding: utf-8 -*-
from random import choice
import os
 
class Color:
    def __init__(self, filename=None):
        """
        
        Paramètre
        ---------

            filename: nom du fichier contenant les couleurs
                      par défaut: None
                      Si None, on lit le fichier 'data/rgb.txt' se 
                      trouvant dans ballPack.

        """
        if filename is None:
            filename = os.path.dirname(__file__) + '/data/rgb.txt'

        with open(filename, 'r') as lines:
            self.colorNames = [c.split('\t')[-1].strip('\n') for c in lines]

    def __str__(self):
        return str(self.colorNames)

    def getRandomColor(self):
        """
        renvoie de manière aléatoire le nom d'une couleur
        se trouvant dans la liste colorNames.
        """
        return choice(self.colorNames)
 
    def getColor(self, i):
        """
        renvoie le nom de la couleur du ième
        élément de la liste colorNames.
        """
        if i >=0 and i<len(self.colorNames):
            return self.colorNames[i]
 
if __name__ == '__main__':
    color = Color('data/rgb.txt')
    print(color.getRandomColor())
    print(color.getColor(10000))
