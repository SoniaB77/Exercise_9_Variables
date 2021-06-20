from math import pi, tan, cos

g = 9.81
vo = 44
theta = 80 * (pi/180)
x = 0.5
yo = 1

y = (yo + x * tan(theta)) - (g * x ** 2) / (2 * (vo * cos(theta)) ** 2)
print(y)
