import math
print("Input float number/-s below.")
while True:
    try:
        l=float(input("Length = "))
        b=float(input("Breadth = "))
        break
    except ValueError:
        print("Please enter valid float numbers.")
d=math.sqrt((l*l)+(b*b))
p=2*(l+b)
a=l*b
print("Diagonal =",d,"unit")
print("Perimeter =",p,"unit")
print("Area =",a,"unit²")
input("Press Enter key to exit")
