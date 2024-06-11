#wap to enter a 5 digit number and print the digit present at odd locations

list1=[]
a = int(input("ENTer 5 digit number : "))
while(a!=0):
    y = a%10
    a=int(a/10)
    list1.append(a)
print("Number at odd position")
for i in range(len(list1)-1,-1,-2):
    print(list[i])