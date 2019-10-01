import math

class Calculator:
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = yS
    '''
    def Add(self):
        """Function for adding numbers"""
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        return num1 + num2

    def Add3(self):
        """Function for adding numbers"""
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        return num1 + num2 + 3
    
    def Subtract(self):
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        return num1 - num2

    def Multiply(self):
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        return num1 * num2

    def Divide(self):
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        return num1 / num2

    def Modulo(self):
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        return num1 % num2

class Engineering_calculator(Calculator):
    def Log(self):
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        return math.log(num1,num2)

    def Sqrt(self):
        num1 = int(input("Enter number:"))
        return math.sqrt(num1)

    def Pow(self):
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter power:"))
        return math.pow(num1,num2)

class Programmer_calculator(Calculator):
    def LogicalAND(self):
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        return num1 and num2

    def LogicalOR(self):
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

c = Calculator()
c1 = Engineering_calculator()
c2 = Programmer_calculator()

choice = int(input("Choose operation:"))
if choice == 1: 
    print(c.Add())
elif choice == 2:
    print(c.Subtract())
elif choice == 3:
    print(c.Multiply())
elif choice == 4:
    print(c.Divide())
elif choice == 5:
    print(c.Modulo())
elif choice == 6:
    print(c1.Log())
elif choice == 7:
    print(c1.Sqrt())
elif choice == 8:
    print(c1.Pow())
elif choice == 9:
    print(c2.LogicalAND())
elif choice == 10:
    print(c2.LogicalOR())
else:
    print("Invalid input")



