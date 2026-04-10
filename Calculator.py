def calculator():
    print("--- Simple Python Calculator ---")
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == '+':
        print(f"Result: {num1 + num2}")
    elif operator == '-':
        print(f"Result: {num1 - num2}")
    elif operator == '*':
        print(f"Result: {num1 * num2}")
    elif operator == '/':
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Cannot divide by zero!")
    else:
        print("Invalid operator!")

if __name__ == "__main__":
    calculator()
