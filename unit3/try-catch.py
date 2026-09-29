#Write a python program to handle the invalid input by the user
try:
    num=int(input("Enter a number: "))
    print("You entered", num)
except ValueError:
    print("Invalid input, please enter an integer")
