
import pySynope
import utils

print("superellipse(1, 1, 2) cloud(5)")
se = pySynope.Superellipse(1, 1, 2)
x, y = se.cloud(5)
print(utils.myformat(x))
print(utils.myformat(y))
print(se.area)

print("circle(1) cloud(10)")
circle = pySynope.Circle(1)
x, y = circle.cloud(10)
print(utils.myformat(x))
print(utils.myformat(y))
print(circle.area)
print(circle.perimeter)




