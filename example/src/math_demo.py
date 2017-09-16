import math

def distance(x1, y1, x0, y0):
    z = math.pow(x1 - x0, 2) + math.pow(y1 - y0, 2)
    z = math.sqrt(z)
    return z