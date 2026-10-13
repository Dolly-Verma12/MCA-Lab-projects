import calculations
import text_utils
import report_utils
print("Addition:", calculations.add(10, 20))
print("Subtraction:", calculations.subtract(20, 10))
print("Multiplication:", calculations.multiply(5, 4))
discount = calculations.calculate_discount(1000, 10)
print("Discount:", discount)
#util
text = "Python makes modular programming easier"
print("Word Count:", text_utils.count_words(text))
print("Reversed:", text_utils.reverse_text(text))
print("Uppercase:", text_utils.convert_uppercase(text))
print("Lowercase:", text_utils.convert_lowercase(text))
#report_util
report_utils.generate_report("Ravi", 85)
#advance util
import advanced_utils
print(
    "Factorial:",
    advanced_utils.factorial(5)
)
print(
    "Fibonacci:",
    advanced_utils.fibonacci(7)
)
print(
    "Total:",
    advanced_utils.calculate_sum(10, 20, 30)
)