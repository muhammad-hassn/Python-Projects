# Create a basic calculator that can perform basic arithmetic operations such as addition,
# subtraction, multiplication, and division.Using Functions....

def add(num1,num2):
    return num1 + num2
def substract(num1,num2):
    return num1 - num2
def multiply (num1,num2):
    return num1 * num2
def division(num1,num2):
    return num1 / num2

print("::Welcome a Basic Calculator::")
print("::Please Select an Operator::")
print("::1--ADDITION::")
print("::2--SUBSTRACTION::")
print("::3--MULTIPLICATION::")
print("::4--DIVISION::")

choice = int(input("Enter your Choice(1/2/3/4)  :"))
num1 = float(input("Enter the first number :"))
num2 = float(input("Enter the second number :"))

if choice == 1:
    result = add(num1,num2)
    print(f"Your Answer",result)
elif choice == 2:
    result = substract(num1,num2)
    print(f"Your Answer",result)
elif choice == 3:
    result = multiply(num1,num2)
    print(f"Your Answer",result)    
elif choice == 4:
    result = division(num1,num2)
    print(f"Your Answer",result)
else:
    print("Invalid Choice.Please Try Again")





