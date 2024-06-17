#1) Expected O/P from the following code
data = [10, 501, 22, 37, 100, 999, 87, 351]
result= filter (lambda x:x>4, data)
print(list(result))

#2) Lambda function to check each and every data in the list
data = [10, 'hello', 22, 'world', 100, 'python', 87, 'chatGPT']

# Using lambda function to check if each element is an integer or string
result = list(map(lambda x: 'integer' if isinstance(x, int) else 'string', data))

# Print the result
print(result)


#3)fibonacci series using lambda function
from functools import reduce

# Function to generate Fibonacci series using lambda
def fibonacci_series(n):
    # Use reduce to build the Fibonacci series
    fib_series = reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [1, 1])
    return fib_series

# Generate Fibonacci series for the first 50 elements
fib_50 = fibonacci_series(50)

# Print the result
print(fib_50)


#4)Validation
import re

def validate_email(email):
    # Regular expression for validating an Email
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(regex, email))

def validate_bd_mobile(mobile):
    # Regular expression for validating Bangladesh mobile numbers (e.g., +8801XXXXXXXXX)
    regex = r'^\+8801[3-9]\d{8}$'
    return bool(re.match(regex, mobile))

def validate_us_telephone(telephone):
    # Regular expression for validating USA telephone numbers (e.g., (XXX) XXX-XXXX or XXX-XXX-XXXX)
    regex = r'^(\(\d{3}\)\s|\d{3}-)\d{3}-\d{4}$'
    return bool(re.match(regex, telephone))

def validate_password(password):
    # Regular expression for validating a 16-character alphanumeric password with upper case, lower case, special characters, and numbers
    regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{16}$'
    return bool(re.match(regex, password))

# Testing the functions
emails = ["test@example.com", "invalid-email@", "user@domain.co.in"]
mobiles = ["+8801712345678", "+8801212345678", "+8801812345678"]
telephones = ["(123) 456-7890", "123-456-7890", "123-4567-890"]
passwords = ["Password1234!@#$", "Pass!2word3$", "Aa1!Aa1!Aa1!Aa1!"]

print("Email Validation:")
for email in emails:
    print(f"{email}: {validate_email(email)}")

print("\nBangladesh Mobile Number Validation:")
for mobile in mobiles:
    print(f"{mobile}: {validate_bd_mobile(mobile)}")

print("\nUSA Telephone Number Validation:")
for telephone in telephones:
    print(f"{telephone}: {validate_us_telephone(telephone)}")

print("\nPassword Validation:")
for password in passwords:
    print(f"{password}: {validate_password(password)}")
