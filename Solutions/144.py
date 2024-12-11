from mpmath import *


mp.dps = 100
slope = (mpf(-9.6) - mpf(10.1))/mpf(1.4)
x,y = mpf(1.4), mpf(-9.6)
count = 0

while abs(x) > 0.01 or y < 0:
    
    angleTangent = atan( -4 * x / y)
    angleIncident = atan(slope)
    angleReflection = 2*angleTangent - angleIncident

    slope = tan(angleReflection)
    newX = (2*(slope*x - y)*slope)/(4+slope**2)-x
    newY = slope*newX-slope*x+y

    x,y = newX, newY
    count += 1

print(count)