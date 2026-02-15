# Result check

n1 = float(input("Enter first number:"))
n2 = float(input("Enter second number:"))
operator = input("Enter operation(+,-,*,/):")

if operator == "+":
    result = n1+n2

elif operator == "-":
    result = n1 - n2

elif operator == "*":
    result = n1 * n2

elif operator == "/":
    if n2 == 0:
        print("Undefined")
        result = None
    else:
        result = n1/n2

else:
    print("Invalid operator.")
    result = None

if result is not None:
    print("result =", result)
    if result > 0:
        print("Positive")
    elif result < 0:
        print("Negative")
    else:
        print("Zero")