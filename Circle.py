import math
pi = math.pi
print("Input float number/-s below.")
while True:
    try:
        r=float(input("Radius = "))
        break
    except ValueError:
        print("Please enter valid float numbers.")
c=2*pi*r
a=pi*r*r
print("Circumference =",c,"unit")
print("Area =",a,"unit²")
input("Press Enter key to exit")
