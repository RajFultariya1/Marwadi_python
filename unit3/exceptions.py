try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print(a / b)
except ZeroDivisionError as e:
    print("Division by zero is Not allowed", e)
print("Hello")
