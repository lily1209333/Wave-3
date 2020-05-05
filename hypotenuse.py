from math import sqrt
a = int(input("Enter first side length: "))
b = int(input("Enter second side length: "))
h = sqrt(a**2 + b**2)
print(round(h, 2), "units")
