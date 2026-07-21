import math
print("Input float number/-s below.")
while True:
    try:
        s=float(input("Side = "))
        break
    except ValueError:
        print("Please enter valid float numbers.")
a=math.sqrt(3)*s*s/4
print("Area =",a,"unit²")
input("Press Enter key to exit")
