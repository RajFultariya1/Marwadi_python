class MyNewClass:
 """this class demonstartes the creation of the objects"""
#instance attrtibute
 num = 100
#instance method
 def hello(self):
    print("Hello world")
#creating the object of my new class
obj=MyNewClass()
#print attribute value
print(obj.num)
#calling method hello
obj.hello()
#print docstring
print(MyNewClass.__doc__)
