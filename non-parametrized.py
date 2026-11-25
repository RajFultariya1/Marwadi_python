#Non-parameterized constructor

class Student:
    def __init__(self):
        print("this is non parameterized constructor")
    def show(self,name):
        print("hello",name)

obj=Student()
obj.show("john")
