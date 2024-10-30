# 1. Print numbers from 1 to 20 using a for loop.

# for number in range(1, 21):
#     print(number)


# 2. Use a while loop to print even numbers from 1 to 50.

# number = 1
# while number <= 50:
#     if number % 2 == 0:
#         print(number)
#     number += 1

# 3. Write a program to calculate the sum of all numbers between 1 and 100.

# total_sum = 0


# for number in range(1, 101):
#     total_sum += number 


# print(f"The sum of all numbers between 1 and 100 is: {total_sum}")

# 4. Print the multiplication table of a given number.

# def multiplication_table(number):
#     print(f"Multiplication Table for {number}:")
#     for i in range(1, 11): 
#         result = number * i
#         print(f"{number} x {i} = {result}")


# num = int(input("Enter a number to print its multiplication table: "))


# multiplication_table(num)

# 5. Print all odd numbers between 1 and 100 using a loop.

# print("Odd numbers between 1 and 100:")
# for number in range(1, 101, 2):  
#     print(number)

# 6. Use a for loop to print each character of a string.

# user_string = input("Enter a string: ")


# print("The characters in the string are:")
# for character in user_string:
#     print(character)

# 7. Find the factorial of a number using a while loop.

# def factorial(n):
#     result = 1 
#     count = 1  

    
#     while count <= n:
#         result *= count  
#         count += 1       

#     return result


# num = int(input("Enter a number to calculate its factorial: "))


# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# else:

#     fact = factorial(num)
#     print(f"The factorial of {num} is: {fact}")

# 8. Use a for loop to print numbers from 10 down to 1


# print("Numbers from 10 down to 1:")
# for number in range(10, 0, -1):
#     print(number)

# 9. Write a program to print the first 10 Fibonacci numbers.

# def fibonacci(n):
#     fib_sequence = []  
#     a, b = 0, 1      

#     for _ in range(n):
#         fib_sequence.append(a) 
#         a, b = b, a + b       

#     return fib_sequence



# first_10_fibonacci = fibonacci(10)
# print("The first 10 Fibonacci numbers are:")
# print(first_10_fibonacci)

# 10. Use a loop to count the number of digits in an integer.
# Function to count the number of digits in an integer
# def count_digits(n):
#     count = 0  # Initialize digit count
#     # Handle the case for negative numbers
#     n = abs(n)

#     # Use a loop to count the digits
#     while n > 0:
#         n //= 10  # Remove the last digit
#         count += 1  # Increment the count

#     return count

# # Input from the user
# num = int(input("Enter an integer: "))

# # Count and display the number of digits
# if num == 0:
#     print("The number of digits in 0 is: 1")
# else:
#     digit_count = count_digits(num)
#     print(f"The number of digits in {num} is: {digit_count}")

# 11. Print the reverse of a given number.
# Function to reverse a number
# def reverse_number(n):
#     reversed_num = 0  # Initialize the reversed number
#     n = abs(n)  # Handle negative numbers by taking the absolute value

#     while n > 0:
#         digit = n % 10  # Get the last digit
#         reversed_num = reversed_num * 10 + digit  # Build the reversed number
#         n //= 10  # Remove the last digit from n

#     return reversed_num

# # Input from the user
# num = int(input("Enter a number: "))

# # Get the reversed number
# reversed_num = reverse_number(num)

# # Print the result
# print(f"The reverse of {num} is: {reversed_num}")


# 12. Print all prime numbers between 1 and 50.

# def is_prime(num):
#     if num <= 1:
#         return False 
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False  
#     return True  


# print("Prime numbers between 1 and 50:")
# for number in range(1, 51):
#     if is_prime(number):
#         print(number)

# 13. Use nested loops to print a pyramid pattern of *.
# Function to print a pyramid pattern of *
# def print_pyramid(rows):
#     for i in range(1, rows + 1):  # Loop for each row
#         # Print spaces
#         for j in range(rows - i):  # Print spaces before the stars
#             print(" ", end="")
#         # Print stars
#         for k in range(2 * i - 1):  # Print stars
#             print("*", end="")
#         # Move to the next line after each row
#         print()

# # Specify the number of rows for the pyramid
# num_rows = int(input("Enter the number of rows for the pyramid: "))
# print_pyramid(num_rows)

# 14. Write a program that breaks the loop when a certain condition is met.
# Program to break a loop when a certain condition is met
# while True:  # Infinite loop
#     user_input = int(input("Enter a number (0 to exit): "))
    
#     if user_input == 0:  # Condition to break the loop
#         print("Exiting the loop...")
#         break  # Break the loop when the user enters 0
    
#     print(f"You entered: {user_input}")

# 15. Print the sum of even and odd numbers separately up to a given number.

# def sum_even_odd(n):
#     even_sum = 0  
#     odd_sum = 0   

#     for number in range(1, n + 1): 
#         if number % 2 == 0:  
#             even_sum += number 
#         else:  
#             odd_sum += number 

#     return even_sum, odd_sum

# num = int(input("Enter a number: "))


# even_sum, odd_sum = sum_even_odd(num)


# print(f"Sum of even numbers up to {num} is: {even_sum}")
# print(f"Sum of odd numbers up to {num} is: {odd_sum}")

# 16. Create a program to calculate the sum of the digits of an inputted integer.


# def sum_of_digits(n):
#     digit_sum = 0  
#     n = abs(n)  

#     while n > 0:
#         digit_sum += n % 10  
#         n //= 10 

#     return digit_sum

# num = int(input("Enter an integer: "))

# result = sum_of_digits(num)


# print(f"The sum of the digits of {num} is: {result}")

# 17. Write a program that continues to ask for a number until the correct number is guessed.

# Program to guess a number
# def guess_number(correct_number):
#     while True:  # Infinite loop to keep asking for a number
#         user_guess = int(input("Guess the number (between 1 and 100): "))
        
#         if user_guess < correct_number:
#             print("Too low! Try again.")
#         elif user_guess > correct_number:
#             print("Too high! Try again.")
#         else:
#             print("Congratulations! You've guessed the correct number!")
#             break  


# correct_number = 42  # Example number to guess


# guess_number(correct_number)

# 18. Use a loop to print numbers in reverse order within a given range.


# def print_reverse_range(start, end):
#     for number in range(end, start - 1, -1):  
#         print(number)


# start_num = int(input("Enter the start of the range: "))
# end_num = int(input("Enter the end of the range: "))


# print(f"Numbers in reverse order from {end_num} to {start_num}:")
# print_reverse_range(start_num, end_num)

# 19. Use a for loop to print the square of each number from 1 to 10.


# def print_squares():
#     for number in range(1, 11): 
#         square = number ** 2  
#         print(f"The square of {number} is: {square}")


# print_squares()

# 20. Create a program that simulates a countdown timer starting from a given number down to zero.

# import time  # Import the time module to create a delay

# # Function to simulate a countdown timer
# def countdown_timer(start):
#     print(f"Countdown starting from {start}...")
#     for number in range(start, -1, -1):  # Loop from start down to 0
#         print(number)  # Print the current number
#         time.sleep(1)  # Pause for 1 second


# start_number = int(input("Enter the starting number for the countdown: "))


# countdown_timer(start_number)




