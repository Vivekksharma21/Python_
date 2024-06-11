#wap to enter a string and print it in reverse also print the no. of vowels and consonant in it

x = input("Enter a string ")
print(x)
a = x.split()
print(a)
b = len(a)-1
list1=[]
while b>=0:
    list1.append(a[b])
    b= b-1
out = " ".join(list1)
print("After reversing : ",out)

c = ['a','e','i','o','u','A','E','I','O','U']
vowels = 0
consonant = 0
for i in x :
    if i in c:
        vowels = vowels+1
    else :
        consonant = consonant+1
print("Vowels are : ",vowels)
print("consonant are : ",consonant)
