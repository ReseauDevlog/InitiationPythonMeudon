# coding: utf8

class Point3d:
    
  @property
  def x(self):
    return self.__x

  @x.setter
  def x(self, value):
    self.__x = value

  @property
  def y(self):
    return self.__y

  @y.setter
  def y(self, value):
    self.__y = value

  @property
  def z(self):
    return self.__z

  @z.setter
  def z(self, value):
    self.__z = value

  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def opposite(self):
    return Point3d(-self.x, -self.y, -self.z)

  def __mul__(self, real):
    return Point3d(-self.x*real, -self.y*real, -self.z*real)
  
  def __str__(self):
    return '({:+.2f}, {:+.2f}, {:+.2f})'.format(self.x,self.y,self.z)


