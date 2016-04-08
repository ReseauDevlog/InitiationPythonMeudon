from __future__ import print_function
import pySynope
import math

q = pySynope.Quaternion()
print(q)

q.set_angle(math.pi/4)
q.normalize()
print(q)

print((q*q).rotate([1, 0, 0]))
