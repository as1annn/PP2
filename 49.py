#Ex 1
from functools import reduce
def multiply_list(numbers):
    if numbers:
        result = reduce(lambda x, y: x * y, numbers)
        return result
    else:
        return None
numbers_list = [10, 20, 30, 40, 50]
result = multiply_list(numbers_list)
print(result)
#Ex2
def count_upper_lower(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count

input_string = "Hello Kbtu"
upper, lower = count_upper_lower(input_string)
print(upper)
print(lower)
#Ex3
def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]
input_string = "A man, a plan, a canal: Panama"
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
#Ex4
import time
import math

def root(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    return result
number = 25100
milliseconds = 2123
result = root(number, milliseconds)
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")
#Ex 5 
def all_true(tuple_var):
    return all(tuple_var)

tuple_var = (True, True, True)
result = all_true(tuple_var)
print(result)

tuple_var = (True, False, True)
result = all_true(tuple_var)
print(result)





