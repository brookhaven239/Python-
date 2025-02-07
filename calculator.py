
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")


    def add(x, y):
        print(x+y)

    def subtract(x, y):
        print(x - y)


    def multiply(x, y):
        print(x * y)


    def divide(x, y):
        if y != 0:
            print(x / y)
        else:
            return "Error! Division by zero."


    operator = input("Enter operator (1/2/3/4): ")


    if operator in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operator == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif operator == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif operator == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif operator == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid Input")

calculator()
