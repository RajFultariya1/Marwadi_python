#write a python program to use the try-except-else-finally blocks
try:
    num=int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("You entered", num)
finally:
    print("This finally block will always execute")