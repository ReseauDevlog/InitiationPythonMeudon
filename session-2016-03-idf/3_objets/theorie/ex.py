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
#print(list(map(fois5plus4,[1,5,10,20,50])))




class Vecteur(object):
    def __init__(self,u=0,v=0,w=0):
        self.__x = u
        self.__y = v
        self.__z = w
        
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
 
    def __getitem__(self, index):
        coords = [self.__x,  self.__y,  self.__z]
        return coords[index]
  
 
    def __str__(self):
        return "({:.0f},{:.0f},{:.0f})".\
           format(self.__x, self.__y,  self.__z)


class Movement(object):
    def __init__(self,x=0,y=0,z=0,m=0):
        self._vitesse = Vecteur(x,y,z)
        self._masse = m


    def __str__(self):
        return "{}|{:d}".format(self._vitesse.__str__(), self._masse)


    def __eq__(self,other): 
        return ( self._vitesse==other._vitesse ) and ( self._masse==other._masse )


class Impulsion(Movement):
    def __getitem__(self, index):
        return self._masse * self._vitesse[index]
         
    

imp = Impulsion(12,22,2,5)

print(imp)

print ('Imp_z', imp[2] )

for i in imp:
    print (i) 


"""





#v1 = Vecteur(8, 3)
#v2 = Vecteur(-1, 7)
#v3 = v1 * v2
#
#print(v3)


   
"""