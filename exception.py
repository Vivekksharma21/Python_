try:
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    if(b==0):
        raise ZeroDivisionError;
    else:
        print("a/b = ",a/b)
except ZeroDivisionError:
    print("b can not be 0 ")