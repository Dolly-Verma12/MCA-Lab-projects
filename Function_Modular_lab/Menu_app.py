import calculations
import text_utils
import report_utils
import advanced_utils
while True:
    print("\n===== REUSABLE SOFTWARE COMPONENTS =====")
    print("1. Mathematical Calculations")
    print("2. Text Processing")
    print("3. Employee Report")
    print("4. Factorial")
    print("5. Fibonacci")
    print("6. Variable Argument Calculation")
    print("7. Exit")
    print("=========================================")
    choice = input("Enter your choice: ")
    if choice == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Addition:", calculations.add(a, b))
        print("Subtraction:", calculations.subtract(a, b))
        print("Multiplication:", calculations.multiply(a, b))

    elif choice == "2":
        text = input("Enter text: ")
        print("Word Count:", text_utils.count_words(text))
        print("Uppercase:", text_utils.convert_uppercase(text))
        print("Lowercase:", text_utils.convert_lowercase(text))

    elif choice == "3":
        name = input("Enter employee name: ")
        score = float(input("Enter performance score: "))
        report_utils.generate_report(name, score)
    elif choice == "4":
        number = int(input("Enter a number: "))
        print("Factorial:", advanced_utils.factorial(number))
    elif choice == "5":
        number = int(input("Enter Fibonacci position: "))
        print("Fibonacci Value:", advanced_utils.fibonacci(number))
    elif choice == "6":
        numbers = input("Enter numbers separated by spaces: ")
        numbers = [float(number) for number in numbers.split()]
        print("Total:", advanced_utils.calculate_sum(*numbers))
    elif choice == "7":
        print("Thank you for using the modular application.")
        break

    else:

        print("Invalid choice. Please select an option from 1 to 7.")