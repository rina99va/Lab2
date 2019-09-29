import math

class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def Add():
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        return num1 + num2

    def Subtract():
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        return num1 - num2

    def Multiply():
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        return num1 * num2

    def Divide():
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        return num1 / num2

    def Modulo():
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        return num1 % num2

class Engineering_calculator(Calculator):
    def Log():
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        return math.log(num1,num2)

    def Sqrt():
        num1 = int(input("Enter number:"))
        return math.sqrt(num1)

    def Pow():
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter power:"))
        return math.pow(num1,num2)

class Programmer_calculator(Calculator):
    def LogicalAND():
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        return num1 and num2

    def LogicalOR():
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        return num1 or num2

print("1.Calculator")
print("2.Engineering calculator")
print("3.Proggrammer calculator")
a = int(input("Choose calculator:"))

if a == 1:
    print("Select operation:")
    print("1:Add")
    print("2:Subtract")
    print("3:Multiply")
    print("4:Divide")
    print("5:Modulo")
if a == 2:
    print("6:Log")
    print("7:Squere")
    print("8:Power")
if a == 3:
    print("9:Logical AND")
    print("10:Logical OR")

choice = int(input("Choose operation:"))
if choice == 1:
    print(Calculator.Add())
elif choice == 2:
    print(Calculator.Subtract())
elif choice == 3:
    print(Calculator.Multiply())
elif choice == 4:
    print(Calculator.Divide())
elif choice == 5:
    print(Calculator.Modulo())
elif choice == 6:
    print(Engineering_calculator.Log())
elif choice == 7:
    print(Engineering_calculator.Sqrt())
elif choice == 8:
    print(Engineering_calculator.Pow())
elif choice == 9:
    print(Programmer_calculator.LogicalAND())
elif choice == 10:
    print(Programmer_calculator.LogicalOR())
else:
    print("Invalid input")



