#write a python program to use the try-except-else blocks
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("You entered", num)