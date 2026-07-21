print("Input float number/-s below.")
while True:
    try:
        l1=float(input("First leg = "))
        l2=float(input("Second leg = "))
        break
    except ValueError:
        print("Please enter valid float numbers.")
a=1/2*l1*l2
print("Area =",a,"unit²")
input("Press Enter key to exit")
