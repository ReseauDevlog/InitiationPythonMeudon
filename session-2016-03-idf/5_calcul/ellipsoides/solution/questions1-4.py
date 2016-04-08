from pylab import *

from pySynope.utils import *
import numpy as np
from pySynope.ellipsoides.superellipse import Superellipse



theta = np.linspace(1,6,12)
print(spe_cos(theta, 2))
print ('-'* 20)
print(spe_sin(theta, 2))





c = Superellipse(1, 1, 100)
x, y = c.cloud(100)
print(x,y)
plot(x, y, '.')
show()
