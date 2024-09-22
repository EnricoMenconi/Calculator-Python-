import math


def calculator():
    print("Hello, future employer (I hope)! Welcome to my advanced calculator with real numbers!")

    while True:
        print("\nPlease choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation. It's getting serious now...")
        print("6. Square Root")
        print("7. Exit")

        choice = input("Enter the number corresponding to the operation: ")

        if choice == '7':
            print("Already? Exiting the calculator. I guess you're on your way to hiring me now...")
            break

        # Inicializando number1 e number2
        number1 = None
        number2 = None

        if choice in ['1', '2', '3', '4', '5']:
            number1 = float(input("Please, type the first number: "))
            number2 = float(input("Please, type the second number: "))

        if choice == '1':
            result = number1 + number2
            print(f"The sum of the numbers is {result}. That one was too easy!")

        elif choice == '2':
            result = number1 - number2
            print(f"The subtraction of the numbers is {result}.")

        elif choice == '3':
            result = number1 * number2
            print(f"The multiplication of the numbers is {result}.")

        elif choice == '4':
            if number2 != 0:
                result = number1 / number2
                print(f"The division of the numbers is {result}. Try again and don't forget to hire me!")
            else:
                print("Error: Division by zero is not allowed.")

        elif choice == '5':
            result = number1 ** number2
            print(f"The result of {number1} raised to the power of {number2} is {result}.")

        elif choice == '6':
            number = float(input("Now we are talking! Please, type the number for which you want the square root: "))
            if number >= 0:
                result = math.sqrt(number)
                print(f"The square root of {number} is {result}.")
            else:
                print("Error: Cannot compute the square root of a negative number.")

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    calculator()

