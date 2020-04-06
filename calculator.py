# Better calculator
first_num = float(input("Enter first number: "))
operator = input("Enter operator: ")
second_num = float(input("Enter second number: "))

if operator == "+":
    print(first_num + second_num)
elif operator == "-":
    print(first_num - second_num)
elif operator == "/":
    print(first_num / second_num)
elif operator == "*":
    print(first_num * second_num)
else:
    print("You entered an invalid operator")
