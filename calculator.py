def addition(a, b):
    return a + b


def multiplication(a, b):
    return a * b


def main():
    # Ask the user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform addition
    result = addition(num1, num2)
    result_multiplication = multiplication(num1, num2)

    # Display the result
    print(f"The sum of {num1} and {num2} is: {result}")
    print(f"The product of {num1} and {num2} is: {result_multiplication}")


if __name__ == "__main__":
    main()
