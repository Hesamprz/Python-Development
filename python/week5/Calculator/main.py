import module


operations = {
    "add": module.add,
    "subtract": module.subtract,
    "multiply": module.multiply,
    "divide": module.divide,
    "sqrt": module.sqrt,
    "sin": module.sin,
    "cos": module.cos,
    "tan": module.tan,
    "cot": module.cot
}

while True:
    try:
        operation = input("Enter the operation (add, subtract, multiply, divide, sqrt, sin, cos, tan, cot) or 'exit' to quit: ")
        if operation == 'exit':
            break
        if operation not in operations:
            raise ValueError("Invalid operation")
        if operation in ["add", "subtract", "multiply", "divide"]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = operations[operation](num1, num2)
        elif operation == "sqrt":
            num = float(input("Enter the number: "))
            result = operations[operation](num)
        else:
            angle = float(input("Enter the angle in degrees: "))
            result = operations[operation](angle)

        print(f"The result of {operation} is: {result}")

    except:
        print("Something went wrong!")

