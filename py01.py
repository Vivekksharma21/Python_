import math
a = int(input("ENter the value of a : "))
b = int(input("ENter the value of b : "))
c = int(input("Enter the value of c : "))
s = float(a+b+c)/2
z = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle : ",z)