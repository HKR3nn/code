def calculator():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the first number: "))
    operator = input("pilih operator  (+, -, *, /): ")
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif  operator == "*":
        print(num1 * num2)
    elif  operator == "/":
        if num2 != 0:
            print(num1 / num2)
calculator()