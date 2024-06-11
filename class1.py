class Student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def talk(self):
        print("My name is : ",self.name)
        print("Roll no. is : ",self.roll)
        print("Marks is : ",self.marks)

str1 = input("Enter your name :")
rol = int(input("Enter your roll no: "))
mark = int(input("Enter your marks : "))

s = Student(str1,rol,mark)
s.talk()



