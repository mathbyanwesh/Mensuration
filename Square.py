import math
print("Input float number/-s below.")
while True:
    try:
        s=float(input("Side = "))
        break
    except ValueError:
        print("Please enter valid float numbers.")
d=math.sqrt(2)*s
p=4*s
a=s*s
print("Diagonal =",d,"unit")
print("Perimeter =",p,"unit")
print("Area =",a,"unit²")
input("Press Enter key to exit")
