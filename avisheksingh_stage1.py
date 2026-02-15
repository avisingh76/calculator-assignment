# Basic Calculator

n1 = float(input("Enter first number:"))
n2 = float(input("Enter second number:"))
operator = input("Enter operation(+,-,*,/):")

if operator == "+":
    result = n1+n2
    print("result:",result)
elif operator == "-":
    result =n1-n2
    print("result:",result)
elif operator == "*":
    result =n1*n2
    print("result:",result)
elif operator == "/":
    if n2 == 0:
        print("Undefined")
    else:
        result =n1/n2
        print("result:",result)

else:
    print("Invalid operation!")
