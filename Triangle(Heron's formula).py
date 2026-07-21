import math
print("Input float number/-s below.")
while True:
    try:
        s1=float(input("First side = "))
        s2=float(input("Second side = "))
        s3=float(input("Third side = "))
        break
    except ValueError:
        print("Please enter valid float numbers.")
s=1/2*(s1+s2+s3)
a=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print("Area =",a,"unit²")
input("Press Enter key to exit")
