print("Input float number/-s below.")
while True:
    try:
        s=float(input("Side = "))
        d1=float(input("First diagonal = "))
        d2=float(input("Second diagonal = "))
        break
    except ValueError:
        print("Please enter valid float numbers.")
p=4*s
a=1/2*d1*d2
print("Perimeter =",p,"unit")
print("Area =",a,"unit²")
input("Press Enter key to exit")
