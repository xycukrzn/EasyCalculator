class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            raise ValueError("Cannot divide by zero!")


def main():
    calculator = Calculator()

    print("Welcome to Calculator!")

    while True:
        print("Select an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            result = calculator.add(x, y)
            print("Result: ", result)
        elif choice == '2':
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            result = calculator.subtract(x, y)
            print("Result: ", result)
        elif choice == '3':
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            result = calculator.multiply(x, y)
            print("Result: ", result)
        elif choice == '4':
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            try:
                result = calculator.divide(x, y)
                print("Result: ", result)
            except ValueError as e:
                print(e)
        elif choice == '5':
            print("Thank you for using Calculator!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()