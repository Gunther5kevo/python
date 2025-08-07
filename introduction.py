
num1=float(input("enter the first number"))
num2=float(input("enter the second number"))
calculation = input("Enter the operation (+,-,*, /):")
if calculation == "+":
    print(num1, "+", num2, "=",num1+num2)
elif calculation == "-":
    print(num1, "-", num2, "=", num1-num2)
elif calculation == "*":
    print(num1, "*", num2, "=", num1 * num2)
elif calculation == "/":
    print(num1, "/", num2, "=", num1 / num2)
else:
    print("invalid ")