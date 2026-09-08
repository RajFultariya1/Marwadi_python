#Python program to create an function ()
'''
def area_of_circle(radius);
    area = 3.14 * radius * radius
    return area

r=5
result = area_of_circle(r)

print("Radius =",r)
print("Area of circle =",r)'''

#Function definition
'''
def calculate_area(width,height):
    return width * height

width = 10
height = 5


total_length=calculate_area(width,height)
print("width:" ,width)
print("height:",height)
print("Calculated length:" ,total_length)
'''

#Positional arguments
'''
def student(name,age):
    print("Name : ",name)
    print("Age : ",age)

student("Vashi",21)'''

#Default argument

def greet(name="student"):
    print("hello",name)

greet()
greet("hello")
