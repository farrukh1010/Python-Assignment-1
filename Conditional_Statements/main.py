# 1. Write a program that checks if a given number is positive, negative, or zero.


# def check_number(num):
#     if num > 0:
#         return "Positive"
#     elif num < 0:
#         return "Negative"
#     else:
#         return "Zero"


# number = int(input("Enter a number: "))

# result = check_number(number)
# print(f"The number is {result}.")

# 2. Take a user’s age as input and display whether they are a minor, adult, or senior citizen.

# def age_category(age):
#     if age < 18:
#         return "Minor"
#     elif 18 <= age < 65:
#         return "Adult"
#     else:
#         return "Senior Citizen"


# age = int(input("Enter your age: "))


# category = age_category(age)
# print(f"You are a {category}.")

# 3. Write a program that checks if a given year is a leap year.


# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False


# year = int(input("Enter a year: "))


# if is_leap_year(year):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

# 4. Take an integer and check if it’s even or odd.

# Function to check if a number is even or odd

# def check_even_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"


# number = int(input("Enter an integer: "))


# result = check_even_odd(number)
# print(f"The number is {result}.")

# 5. Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).

# def get_letter_grade(percentage):
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 80:
#         return "B"
#     elif percentage >= 70:
#         return "C"
#     elif percentage >= 60:
#         return "D"
#     else:
#         return "F"


# percentage = float(input("Enter your grade percentage: "))

# letter_grade = get_letter_grade(percentage)
# print(f"Your letter grade is: {letter_grade}")

# 6. Write a program to find the largest of two numbers.


# def find_largest(num1, num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2


# number1 = float(input("Enter the first number: "))
# number2 = float(input("Enter the second number: "))

# largest = find_largest(number1, number2)
# print(f"The largest number is: {largest}")

# 7. Write a program to find the largest of three numbers.


# def find_largest(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3


# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))


# largest = find_largest(number1, number2, number3)
# print(f"The largest number is: {largest}")

# 8. Create a program that checks if a given string is a palindrome.


# def is_palindrome(s):
#     # Convert the string to lowercase and remove spaces for accurate comparison
#     s = s.replace(" ", "").lower()
#     return s == s[::-1]  # Check if the string is equal to its reverse

# string = input("Enter a string: ")


# if is_palindrome(string):
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

# 9. Take three sides of a triangle as input and check if they form a valid triangle.


# def is_valid_triangle(a, b, c):
#     # A triangle is valid if the sum of any two sides is greater than the third side
#     return (a + b > c) and (a + c > b) and (b + c > a)

# # Input from the user
# side1 = float(input("Enter the first side: "))
# side2 = float(input("Enter the second side: "))
# side3 = float(input("Enter the third side: "))

# # Checking if the sides form a valid triangle
# if is_valid_triangle(side1, side2, side3):
#     print("The sides form a valid triangle.")
# else:
#     print("The sides do not form a valid triangle.")

# 10. Write a program to determine if a given character is a vowel or consonant.


# def check_vowel_consonant(char):
#     vowels = "aeiouAEIOU"  # Define vowels for both uppercase and lowercase
#     if char in vowels:
#         return "Vowel"
#     else:
#         return "Consonant"

# # Input from the user
# character = input("Enter a character: ")

# # Validating that the input is a single alphabetic character
# if len(character) == 1 and character.isalpha():
#     # Checking if the character is a vowel or consonant
#     result = check_vowel_consonant(character)
#     print(f"The character is a {result}.")
# else:
#     print("Please enter a single alphabetic character.")

# 11. Check if a given number is a multiple of both 3 and 5.



# def is_multiple_of_3_and_5(number):
#     return number % 3 == 0 and number % 5 == 0


# number = int(input("Enter a number: "))

# if is_multiple_of_3_and_5(number):
#     print(f"{number} is a multiple of both 3 and 5.")
# else:
#     print(f"{number} is not a multiple of both 3 and 5.")

# 12. Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.



# def check_temperature_category(temperature):
#     if temperature <= 0:
#         return "Freezing"
#     elif 0 < temperature < 30:
#         return "Moderate"
#     else:
#         return "Hot"


# temperature = int(input("Enter the temperature in Celsius: "))

# category = check_temperature_category(temperature)
# print(f"The temperature is categorized as: {category}.")

# 13. Take two numbers and an operator (+, -, *, /) as input and perform the corresponding operation.

# def calculate(num1, num2, operator):
#     if operator == '+':
#         return num1 + num2
#     elif operator == '-':
#         return num1 - num2
#     elif operator == '*':
#         return num1 * num2
#     elif operator == '/':
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return "Error: Division by zero is not allowed."
#     else:
#         return "Error: Invalid operator."


# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# operator = input("Enter an operator (+, -, *, /): ")


# result = calculate(number1, number2, operator)
# print(f"The result is: {result}")


# 14. Check if a year input by the user is a century year.


# def is_century_year(year):
#     return year % 100 == 0

# year = int(input("Enter a year: "))


# if is_century_year(year):
#     print(f"{year} is a century year.")
# else:
#     print(f"{year} is not a century year.")

# 15. Write a program to check if a number is within a specified range.

# Function to check if a number is within a specified range
# def is_within_range(number, lower_bound, upper_bound):
#     return lower_bound <= number <= upper_bound

# # Input from the user
# number = int(input("Enter a number: "))
# lower_bound = int(input("Enter the lower bound of the range: "))
# upper_bound = int(input("Enter the upper bound of the range: "))


# if is_within_range(number, lower_bound, upper_bound):
#     print(f"{number} is within the range of {lower_bound} and {upper_bound}.")
# else:
#     print(f"{number} is not within the range of {lower_bound} and {upper_bound}.")

# 16. Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).

# Function to classify the triangle based on the lengths of its sides
# def classify_triangle(a, b, c):
#     if a == b == c:
#         return "Equilateral"
#     elif a == b or b == c or a == c:
#         return "Isosceles"
#     else:
#         return "Scalene"

# # Input from the user
# side1 = int(input("Enter the length of the first side: "))
# side2 = int(input("Enter the length of the second side: "))
# side3 = int(input("Enter the length of the third side: "))

# # Checking if the sides form a valid triangle
# if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
#     # Classifying and displaying the triangle type
#     triangle_type = classify_triangle(side1, side2, side3)
#     print(f"The triangle is {triangle_type}.")
# else:
#     print("The lengths entered do not form a valid triangle.")

# 17. Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.

# Function to check divisibility
# def check_divisibility(number):
#     divisible_by_2 = number % 2 == 0
#     divisible_by_3 = number % 3 == 0

#     return divisible_by_2, divisible_by_3

# # Input from the user
# number = int(input("Enter an integer: "))

# # Checking divisibility
# divisible_by_2, divisible_by_3 = check_divisibility(number)

# # Displaying the results
# if divisible_by_2 and divisible_by_3:
#     print(f"{number} is divisible by both 2 and 3.")
# elif divisible_by_2:
#     print(f"{number} is divisible by 2.")
# elif divisible_by_3:
#     print(f"{number} is divisible by 3.")
# else:
#     print(f"{number} is not divisible by 2 or 3.")

# 18. Take a user’s score and determine if they pass or fail (pass if 50 or above).

# Function to check if the score is a pass or fail
# def check_pass_fail(score):
#     return score >= 50


# score = int(input("Enter your score: "))


# if check_pass_fail(score):
#     print("You passed!")
# else:
#     print("You failed.")

# 19. Check if a string input is uppercase, lowercase, or a mix.

# Function to check the case of the string


# def check_string_case(s):
#     if s.isupper():
#         return "Uppercase"
#     elif s.islower():
#         return "Lowercase"
#     else:
#         return "Mix of Uppercase and Lowercase"


# user_input = input("Enter a string: ")

# case_type = check_string_case(user_input)
# print(f"The string is: {case_type}.")

# 20. Create a program that evaluates if an inputted number is prime.

# Function to check if a number is prime
# def is_prime(number):
#     if number <= 1:
#         return False  # Numbers less than or equal to 1 are not prime
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False  # Found a divisor, so it's not prime
#     return True  # No divisors found, it's prime

# # Input from the user
# num = int(input("Enter a number: "))

# # Checking if the number is prime
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")
