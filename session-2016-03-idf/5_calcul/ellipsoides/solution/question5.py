from pylab import *
from mpl_toolkits.mplot3d import axes3d
from pySynope.utils import *
import numpy as np
from pySynope.ellipsoides.superellipse import Superellipse
from pySynope.ellipsoides.superellipsoid import Superellipsoid



theta = np.linspace(1,6,12)
print(spe_cos(theta, 2))
print ('-'* 20)
print(spe_sin(theta, 2))





c = Superellipse(10, 2, 100)
#x, y = c.cloud(100)
x, y = c.cloud_with_square(10)
#print(x,y)
plot(x, y, '.')
show()


c = Superellipsoid(1, 1, 1, 1, 1)
x, y, z = c.cloud_with_square(10)

fig = figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x, y, z, color='b')
plt.show()