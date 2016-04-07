# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:06:08 2016

@author: dmitry
"""

class FonctionLineaire(object):
    def __init__(self, a, b=0):
        self.a, self.b = a, b    
    def __call__(self, x):
        return self.a * x + self.b
    
fois5plus4 = FonctionLineaire(5,4)
print(list(map(fois5plus4,[1,5,10,20,50])))




class Vecteur(object):
    def __init__(self,u=0,v=0):
        self.__x = u
        self.__y = v
        
    def __add__(self, other):
        if isinstance(other, Vecteur):
          newx = self.__x + other.__x
          newy = self.__y + other.__y
          return Vecteur(newx, newy)

    def __mul__(self, other):
        if isinstance(other, Vecteur):
          newx = self.__x * other.__x
          newy = self.__y * other.__y
          return Vecteur(newx, newy)
  
    def __str__(self):
        return "({:.0f},{:.0f})".format(self.__x, self.__y)


v1 = Vecteur(8, 3)
v2 = Vecteur(-1, 7)
v3 = v1 * v2

print(v3)







"""
      def __getitem__(self, index):
        coords = [self.__x,  self.__y]
        return coords[index]
  

print (v3[0],v3[1],v3[:], v3[1:])

for i,c in enumerate(v3):
    print ('Coordinate %d: %.1f' % (i,c))



"""