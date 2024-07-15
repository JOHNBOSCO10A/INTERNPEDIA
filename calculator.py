def calculate():
    print("Welcome to the Calculator App!")
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter the operator (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Error: Division by zero!")
                    continue
            else:
                print("Error: Invalid operator!")
                continue

            print("Result: ", result)

        except ValueError:
            print("Error: Invalid input. Please enter a number.")

        else:
            cont = input("Do you want to continue? (y/n): ")
            if cont.lower() != "y":
                break

    print("Farewell! Thanks for using the Calculator App.")

calculate()
