from __future__ import print_function
import pySynope
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as animation
import numpy as np

def animate(i):
  """ 
  Animation par une rotation d'une superellipse.

  Lorsque le nombre d'images est un multiple de 10,
  on change l'axe de rotation.

  """
  ax.clear()
  ax.set_xlim3d(-rmax, rmax)
  ax.set_ylim3d(-rmax, rmax)
  ax.set_zlim3d(-rmax, rmax)

  if i%10 == 0:
    q.set_angle(np.pi/10, np.random.random(3))
    q.normalize()
  
  x[:], y[:], z[:] = q.rotate(np.asarray([x, y, z]))
  ax.plot_wireframe(x, y, z, color='b')  

rx, ry, rz = 1, 1, 1
m1, m2 = 1, 1
c = pySynope.Superellipsoid(rx, ry, rz, m1, m2)
x, y, z = c.cloud_with_square(15)

q = pySynope.Quaternion()
q.set_angle(np.pi/10)

rmax = np.max([rx, ry, rz])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
