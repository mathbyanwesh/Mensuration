import math
print("Input float number/-s below.")
while True:
    try:
        l = float(input("Length = "))
        b = float(input("Breadth = "))
        h = float(input("Height = "))
        break
    except ValueError:
        print("Please enter valid float numbers.")
d = math.sqrt(l*l + b*b + h*h)
a = 2 * (l + b) * h
print("Diagonal =", d, "unit")
print("Area =", a, "unit²")
input("Press Enter key to exit")
