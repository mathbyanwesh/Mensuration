print("Input float number/-s below.")
while True:
    try:
        b=float(input("Base = "))
        h=float(input("Height = "))
        break
    except ValueError:
        print("Please enter valid float numbers.")
p=2*(b+h)
a=b*h
print("Perimeter =",p,"unit")
print("Area =",a,"unit")
input("Press Enter key to exit")
