#Basic If-Else problems

#1.Write a program to check whether a number is positive, negative, or zero.
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number.")
elif num < 0:
    print(" Negative number.")
else:	        
    print("The number is Zero.")

#2. Write a program to check whether a number is even or odd.
num = int(input("Enter an integer: "))
if num % 2 == 0:
    print("Even number.")
else:
    print("Odd number.")

#3. Write a program to check if a given year is a leap year or not.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The entered year is a leap year.")
else:
    print("The entered year is not a leap year.")

#4. Write a program to find the greatest of two numbers.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print("The greatest number is  : ",num1)
elif num2 > num1:
    print("The greatest number is : ",num2)
else :
    print("Both numbers are equal.")

#5. Write a program to check whether a person is eligible to vote (age=18).
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote. ")
else:
    print("You are not eligible to vote yet. ")

#6. Write a program to check whether a given character is a vowel or consonant.
char = input("Enter a single character: ")
if len(char) == 1 and char.isalpha():
    if char in 'aeiouAEIOU':
        print(f"The character '{char}' is a Vowel.")
    else:
        print(f"The character '{char}' is a Consonant.")
else:
    print("Invalid input. Please enter a single alphabet character.")

#7. Write a program to check if a number is divisible by 5.
num = int(input("Enter a number: "))
if num % 5 == 0:
    print(num," : is divisible by 5.")
else:
    print(num, " :  is not divisible by 5.")

#8. Write a program to determine whether a given number is a single-digit, two-digit, or more than two-digit number.
num = int(input("Enter an integer: "))
abs_num = abs(num)
if abs_num < 10:
    print(f"{num} is a single-digit number.")
elif abs_num < 100:
    print("entered number is a two-digit number.")
else:
    print("number has more than two digits.")

#9. Write a program to check whether a student has passed or failed (passing marks = 40).
marks = float(input("Enter the student's marks: "))
if marks >= 40:
    print("Result: Passed!")
else:
    print("Result: Failed.")

#10. Write a program to find whether the entered number is a multiple of both 3 and 7.
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 7 == 0:
    print(f"{num} is a multiple of both 3 and 7.")
else:
    print(f"{num} is not a multiple of both 3 and 7.")	


#Ladder If & Nested If

#1.Write a program to find the greatest among three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3

print(f"The greatest number is : ", greatest)

#2. Write a program to classify a person based on age: Child (<13), Teenager (13-19), Adult (20-59), Senior (60+).
age = int(input("Enter the person's age: "))
if age < 13:
    print("Category: Child")
elif 13 <= age <= 19:
    print("Category: Teenager")
elif 20 <= age <= 59:
    print("Category: Adult")
else: # age >= 60
    print("Category: Senior")

#3. Write a program to assign grades based on marks.
marks = float(input("Enter the marks (0-100): "))
if 90 <= marks <= 100:
    grade = 'A'
elif 75 <= marks <= 89:
    grade = 'B'
elif 50 <= marks <= 74:
    grade = 'C'
elif 35 <= marks <= 49:
    grade = 'D'
elif marks < 35:
    grade = 'Fail'
else:
    grade = 'Invalid Marks'

print(f"Grade: {grade}")

#4. Write a program to check the type of triangle (equilateral, isosceles, or scalene) based on sides.
s1 = float(input("Enter length of side 1: "))
s2 = float(input("Enter length of side 2: "))
s3 = float(input("Enter length of side 3: "))
if s1 == s2 == s3:
    print("It's an Equilateral triangle.")
elif s1 == s2 or s2 == s3 or s1 == s3:
    print("It's an Isosceles triangle.")
else:
    print("It's a Scalene triangle.")

#5. Write a program to check if a character is uppercase, lowercase, digit, or special symbol.
char = input("Enter a single character: ")

if char.isupper():
    print(f"'{char}' is an Uppercase letter.")
elif char.islower():
    print(f"'{char}' is a Lowercase letter.")
elif char.isdigit():
    print(f"'{char}' is a Digit.")
else:
    print(f"'{char}' is a Special Symbol.")

#6. Write a program to calculate electricity bill based on units.
units = int(input("Enter the number of electricity units consumed: "))
bill = 0
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else: 
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10
print("Your total electricity bill is: ", bill)

#7. Write a program to determine the largest of four numbers using nested if.
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
n4 = int(input("Enter fourth number: "))
if n1 > n2:
    if n1 > n3:
        if n1 > n4:
            largest = n1
        else:
            largest = n4
    else: 
        if n3 > n4:
            largest = n3
        else:
            largest = n4
else: 
    if n2 > n3:
        if n2 > n4:
            largest = n2
        else:
            largest = n4
    else: 
        if n3 > n4:
            largest = n3
        else:
            largest = n4
print("The largest number is : ", largest )

#8. Write a program to check if a given year is a century year and also a leap year.
year = int(input("Enter a year: "))
if year % 100 == 0:
    if year % 400 == 0:
        print(f"{year} is a century year and a leap year.")
    else:
        print("Entered year is a century year but not a leap year.")
else:
    print("Entered year is not a century year.")

#9. Write a program to classify BMI value.
bmi = float(input("Enter your BMI value: "))
if bmi < 18.5:
    print("BMI Classification: Underweight")
elif 18.5 <= bmi <= 24.9:
    print("BMI Classification: Normal weight")
elif 25 <= bmi <= 29.9:
    print("BMI Classification: Overweight")
else: # bmi >= 30
    print("BMI Classification: Obese")

#10. Write a program to display the smallest number among three using nested if.
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))
if n1 < n2:
    if n1 < n3:
        smallest = n1
    else:
        smallest = n3
else:
    if n2 < n3:
        smallest = n2
    else: 
        smallest = n3
print("The smallest number is : ",smallest)

#For Loop Problems

#1.Write a program using a for loop to print all Armstrong numbers between 100 and 999.
for num in range(100, 1000):
    s_num = str(num)
    digit1 = int(s_num[0])
    digit2 = int(s_num[1])
    digit3 = int(s_num[2])
    # Calculate sum of cubes of digits
    sum_of_cubes = (digit1 ** 3) + (digit2 ** 3) + (digit3 ** 3)
    if sum_of_cubes == num:
        print(num)
        
#2. Write a program to generate and display the first n prime numbers using a for loop.
n = int(input("How many prime numbers to display? "))
count = 0
num = 2  

print(f"The first {n} prime numbers are:")
while count < n:
    is_prime = True
    # Check for factors from 2 up to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
        count += 1    
    num += 1 

#3. Write a program to display all numbers from 1 to 500 that are divisible by 3, but the sum of their digits should not exceed 10.
for num in range(1, 501):
    if num % 3 == 0:
        temp_num = num
        digit_sum = 0
        while temp_num > 0:
            digit_sum += temp_num % 10
            temp_num //= 10 
        if digit_sum <= 10:
            print(num)

#4. Write a program using a for loop to print a pyramid of stars (*) of height n.
n = int(input("Enter the height of the pyramid: "))
for i in range(n):
    print(" " * (n - 1 - i), end="")
    print("*" * (2 * i + 1))

#5. Write a program to accept a string and check whether it is a pangram.
input_string = input("Enter a string to check for pangram: ").lower()
alphabets = "abcdefghijklmnopqrstuvwxyz"
is_pangram = True
for char in alphabets:
    if char not in input_string:
        is_pangram = False
if is_pangram:
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")

#6. Write a program using a for loop to print all twin primes between 1 and 100.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Twin primes between 1 and 100:")
for num in range(1, 99):
    if is_prime(num) and is_prime(num + 2):
        print(f"({num}, {num + 2})")

#7. Write a program that accepts a number from the user and prints whether it is a Harshad number.
num_str = input("Enter a number: ")
num = int(num_str)
sum_of_digits = 0
for digit in num_str:
    sum_of_digits += int(digit)

if num % sum_of_digits == 0:
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")

#8. Write a program to generate Pascal's Triangle up to n rows using a for loop.
n = int(input("Enter the number of rows for Pascal's Triangle: "))
triangle = []
for i in range(n):
    row = [1] * (i + 1) 
    if i > 1: 
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
    triangle.append(row)
for row in triangle:
    print(" ".join(map(str, row)).center(n * 3))

#9. Write a program using a for loop to display the sum of the series of squares:
n = int(input("Enter the value of n: "))
total_sum = 0
for i in range(1, n + 1):
    total_sum += i ** 2
print(f"The sum of the series up to {n} is: {total_sum}")

#10. Write a program that accepts a number and prints whether it is a Strong number.
import math
num_str = input("Enter a number to check if it's a Strong number: ")
num = int(num_str)
sum_of_factorials = 0
for digit_char in num_str:
    digit = int(digit_char)
    sum_of_factorials += math.factorial(digit)
if sum_of_factorials == num:
    print(f"{num} is a Strong number.")
else:
    print(f"{num} is not a Strong number.")

#While Loop Problems

#1.Write a program using a while loop to find the reverse of a number and check if the reversed number is prime.
num = int(input("Enter a number: "))
temp_num = num
reversed_num = 0
while temp_num > 0:
    digit = temp_num % 10
    reversed_num = (reversed_num * 10) + digit
    temp_num //= 10
print(f"The reverse of {num} is {reversed_num}.")
is_prime = True
if reversed_num <= 1:
    is_prime = False
else:
    for i in range(2, int(reversed_num**0.5) + 1):
        if reversed_num % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{reversed_num} is a prime number.")
else:
    print(f"{reversed_num} is not a prime number.")

#2. Write a program that continues to accept numbers from the user until the sum of digits of all numbers entered becomes greater than 100.
total_digit_sum = 0
while total_digit_sum <= 100:
    print(f"\nCurrent total sum of digits: {total_digit_sum}")
    num_str = input("Enter a number: ")
    current_digit_sum = 0
    for digit in num_str:
        if digit.isdigit():
            current_digit_sum += int(digit)
    total_digit_sum += current_digit_sum
print(f"\nFinal total sum of digits ({total_digit_sum}) has exceeded 100. Halting.")

#3. Write a program using a while loop to check whether a number is a Duck number.
num_str = input("Enter a number: ")
num = int(num_str)
is_duck = False
temp_num = num
while temp_num > 0:
    if temp_num % 10 == 0:
        is_duck = True
        break
    temp_num //= 10
if is_duck:
    print(f"{num} is a Duck number.")
else:
    print(f"{num} is not a Duck number.")

#4. Write a program using a while loop to accept a number and check if it is a Happy number.
num = int(input("Enter a number to check if it's a Happy number: "))
seen_numbers = set()
current_num = num
while current_num != 1 and current_num not in seen_numbers:
    seen_numbers.add(current_num)
    sum_of_squares = 0
    temp_num = current_num
    while temp_num > 0:
        digit = temp_num % 10
        sum_of_squares += digit ** 2
        temp_num //= 10  
    current_num = sum_of_squares
if current_num == 1:
    print(f"{num} is a Happy number")
else:
    print(f"{num} is not a Happy number.")

#5. Write a program using a while loop to find the largest prime factor of a given number.
n = int(input("Enter a number to find its largest prime factor: "))
largest_prime_factor = 0
d = 2 
while d * d <= n:
    while n % d == 0:
        largest_prime_factor = d
        n //= d
    d += 1
if n > 1:
    largest_prime_factor = n
print(f"The largest prime factor is: {largest_prime_factor}")

#6. Write a program to repeatedly accept a string from the user until the string entered is a palindrome.
while True:
    user_string = input("Enter a string: ")
    if user_string == user_string[::-1]:
        print(f"'{user_string}' is a palindrome. Exiting program.")
        break
    else:
        print(f"'{user_string}' is not a palindrome. Please try again.")

#7. Write a program using a while loop to compute the digital root of a number.
num = int(input("Enter a number to find its digital root: "))
while num > 9:
    sum_of_digits = 0
    temp_num = num
    while temp_num > 0:
        sum_of_digits += temp_num % 10
        temp_num //= 10
    num = sum_of_digits 
    print(f"  -> Intermediate sum: {num}")
print(f"The digital root is: {num}")

#8. Write a program using a while loop to generate the Collatz sequence for a given number.
n = int(input("Enter a positive integer for the Collatz sequence: "))
print("The Collatz sequence is:")
while n != 1:
    print(n, end=" -> ")
    if n % 2 == 0: 
        n = n // 2
    else: 
        n = 3 * n + 1
print(1) 

#9. Write a program using a while loop to accept a number and check whether it is a Kaprekar number.
num = int(input("Enter a number to check if it's a Kaprekar number: "))
square = num ** 2
s_square = str(square)
n_digits = len(s_square)
is_kaprekar = False

# Use a while loop to iterate through all possible split points
split_point = 1
while split_point < n_digits:
    part1_str = s_square[:split_point]
    part2_str = s_square[split_point:]
    if part1_str and part2_str:
        part1 = int(part1_str)
        part2 = int(part2_str)  
        if part1 > 0 and part2 > 0 and (part1 + part2 == num):
            is_kaprekar = True
            break  
    split_point += 1
if is_kaprekar:
    print(f"{num} is a Kaprekar number.")
else:
    print(f"{num} is not a Kaprekar number.")

#10. Write a program to simulate an ATM machine using a while loop.
balance = 1000.00 
print("Welcome to the ATM!")
while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")   
    choice = input("Please choose an option (1-4): ")
    if choice == '1':
        print(f"Your current balance is: ₹{balance:.2f}")
    elif choice == '2':
        try:
            deposit_amount = float(input("Enter amount to deposit: "))
            if deposit_amount > 0:
                balance += deposit_amount
                print(f"Successfully deposited ₹{deposit_amount:.2f}.")
                print(f"New balance is: ₹{balance:.2f}")
            else:
                print("Invalid amount. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == '3':
        try:
            withdraw_amount = float(input("Enter amount to withdraw: "))
            if withdraw_amount <= 0:
                print("Invalid amount. Please enter a positive number.")
            elif withdraw_amount > balance:
                print("Insufficient balance to complete this transaction.")
            else:
                balance -= withdraw_amount
                print(f"Please take your cash: ₹{withdraw_amount:.2f}")
                print(f"Remaining balance is: ₹{balance:.2f}")
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please select an option from 1 to 4.")







