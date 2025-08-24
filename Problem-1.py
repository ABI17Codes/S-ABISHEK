
def Calculator(a, b, operation):
    match operation:
        case "add":
            return a + b
        case "subtract":
            return a - b
        case "multiply":
            return a * b
        case "divide":
            if b == 0:
                return "Error: Division by zero is not allowed."
            return a / b
        case _:
            return "Invalid operation. Please choose add, subtract, multiply, or divide."

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")

print("Result:", Calculator(a, b, operation))



