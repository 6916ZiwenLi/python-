from math import pi

r, h = map(float, input().split())
S = pi * r * 2 * (r + h)
print("%.2f" % S)
