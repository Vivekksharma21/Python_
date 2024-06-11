# wap to print even length words in a string :

x = input("Enter a string  : ")
l = x.split()
print(l)
l2 = []
for i in range(1,len(l)):
    if i%2==0:
       l2.append(l[i])
print(l2)