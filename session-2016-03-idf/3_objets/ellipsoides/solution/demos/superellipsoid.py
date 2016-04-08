from __future__ import print_function
import math
import pySynope

s = pySynope.Superellipse(1, 1, 2)
print(s.area)

c = pySynope.Circle(1)
print(c.area)
print(c.perimeter)

s = pySynope.Superellipsoid(1, 1, 1, 2, 2)
print(s.volume, 4./3*math.pi)

s = pySynope.Sphere(1)
print(s.volume, 4./3*math.pi)
