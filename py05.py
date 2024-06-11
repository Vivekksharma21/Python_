a = int(input("Enter a number : "))
print(a)
b = 0
for i in range(1,a):
    if(a%i==0):
        b=b+i
if (b==a):
    print("perfect no. ")
else:
    print("oops! not a perfect no. ")