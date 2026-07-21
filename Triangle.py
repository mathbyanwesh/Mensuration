print("Input float number/-s below.")
while True:
    try:
        b=float(input("Base = "))
        h=float(input("Height = "))
        break
    except ValueError:
        print("Please enter valid float numbers.")
a=1/2*b*h
print("Area =",a,"unit²")
input("Press Enter key to exit")
