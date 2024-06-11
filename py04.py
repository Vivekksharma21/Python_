num = input("Enter a number : ")
num = int(num)

a = num
c = 0

while(num!=0) :
    b = int(num % 10)
    c = (c*10)+b
    num = num//10

if a==c :
    print("Number is palindrome")
else:
    print("Number is not palindrome")

