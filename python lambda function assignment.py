#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Q.1) Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also 
#create a lambda function that multiplies argument x with argument y and prints the result.

# Lambda function to add 15 to a given number
add_15 = lambda x: x + 15
# Lambda function to multiply two numbers
multiply = lambda x, y: x * y
# Sample usage
result1 = add_15(10)
result2 = multiply(4, 12)
print(result1)  
print(result2)


# In[2]:


#Q.2) Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown 
#given number.

def multiply_with_unknown_number(x):
    unknown_number = 5  # You can change this to any desired number
    result = x * unknown_number
    return result

# Sample usage
number = 15
double_result = multiply_with_unknown_number(number)
triple_result = multiply_with_unknown_number(number) * 1.5  # Example of multiplying by 1.5
quadruple_result = multiply_with_unknown_number(number) * 2
quintuple_result = multiply_with_unknown_number(number) * 2.5  # Example of multiplying by 2.5

# Output
print(f"Double the number of {number} = {double_result}")
print(f"Triple the number of {number} = {triple_result}")
print(f"Quadruple the number of {number} = {quadruple_result}")
print(f"Quintuple the number {number} = {quintuple_result}")


# In[3]:


#Q.3) Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples
original_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Sorting the list of tuples based on the second element (marks)
sorted_list = sorted(original_list, key=lambda x: x[1])

# Output
print("Original list of tuples:")
print(original_list)
print("\nSorting the List of Tuples:")
print(sorted_list)


# In[4]:


#Q.4) Write a Python program to sort a list of dictionaries using Lambda.

# Original list of dictionaries
original_list = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

# Sorting the list of dictionaries based on the 'make' key
sorted_list = sorted(original_list, key=lambda x: x['make'])

# Output
print("Original list of dictionaries:")
print(original_list)
print("\nSorting the List of dictionaries:")
print(sorted_list)


# In[5]:


#Q.5) Write a Python program to filter a list of integers using Lambda.

# Original list of integers
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using lambda and filter to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, original_list))

# Using lambda and filter to get odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, original_list))

# Output
print("Original list of integers:")
print(original_list)
print("\nEven numbers from the said list:")
print(even_numbers)
print("Odd numbers from the said list:")
print(odd_numbers)


# In[6]:


#Q.6) Write a Python program to square and cube every number in a given list of

# Original list of integers
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using lambda and map to square every number
squared_numbers = list(map(lambda x: x**2, original_list))

# Using lambda and map to cube every number
cubed_numbers = list(map(lambda x: x**3, original_list))

# Output
print("Original list of integers:")
print(original_list)
print("\nSquare every number of the said list:")
print(squared_numbers)
print("Cube every number of the said list:")
print(cubed_numbers)


# In[7]:


#Q.7) Write a Python program to find if a given string starts with a given character using Lambda.

# Lambda function to check if a string starts with a given character
starts_with_char = lambda string, char: string.startswith(char)

# Sample usage
string1 = "Hello, World!"
char1 = "H"
result1 = starts_with_char(string1, char1)
print(result1)  

string2 = "Python"
char2 = "X"
result2 = starts_with_char(string2, char2)
print(result2)  


# In[8]:


#Q.8) Write a Python program to extract year, month, date and time using Lambda.

from datetime import datetime

# Original datetime string
datetime_string = "2020-01-15 09:03:32.744178"

# Lambda functions to extract year, month, date, and time
extract_year = lambda dt_str: datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S.%f").year
extract_month = lambda dt_str: datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S.%f").month
extract_date = lambda dt_str: datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S.%f").day
extract_time = lambda dt_str: datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S.%f").strftime("%H:%M:%S.%f")

# Output
print(datetime_string)
print(extract_year(datetime_string))
print(extract_month(datetime_string))
print(extract_date(datetime_string))
print(extract_time(datetime_string))


# In[9]:


#Q.9) Write a Python program to check whether a given string is a number or not using Lambda.
# Lambda function to check if a string is a number
is_number = lambda s: s.isdigit() if s.isdigit() else s.count('.') == 1 and s.replace('.', '').isdigit()

# Sample usage
print(is_number("123"))        
print(is_number("3.14"))       
print(is_number("-42"))        
print(is_number("10.5.5"))      
print(is_number("abc"))         


# In[12]:


#Q.10) Write a Python program to create Fibonacci series up to n using Lambda.
#Fibonacci series upto 2=[0, 1]
#Fibonacci series upto 5=[0, 1, 1, 2, 3]
#Fibonacci series upto 6=[0, 1, 1, 2, 3, 5]
#Fibonacci series upto 9=[0, 1, 1, 2, 3, 5, 8, 13, 21]
# Lambda function to generate Fibonacci series up to n
fibonacci_series = lambda n: [0, 1] if n == 2 else fibonacci_series(n - 1) + [fibonacci_series(n - 1)[-1] + fibonacci_series(n - 1)[-2]]

# Sample usage
for i in range(2, 10):
    result = fibonacci_series(i)
    print(f"Fibonacci series upto {i}: {result}")


# In[13]:


#Q.11) Write a Python program to find the intersection of two given arrays using Lambda.
#Original arrays:
#[1, 2, 3, 5, 7, 8, 9, 10]
#[1, 2, 4, 8, 9]
#Intersection of the said arrays: [1, 2, 8, 9]
# Lambda function to find the intersection of two arrays
intersection = lambda array1, array2: list(filter(lambda x: x in array1, array2))

# Original arrays
array1 = [1, 2, 3, 5, 7, 8, 9, 10]
array2 = [1, 2, 4, 8, 9]

# Finding the intersection using the lambda function
result = intersection(array1, array2)

# Output
print("Original arrays:")
print(array1)
print(array2)
print("\nIntersection of the said arrays:")
print(result)


# In[14]:


#Q.12) Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
#Original arrays:
#[-1, 2, -3, 5, 7, 8, 9, -10]
#Rearrange positive and negative numbers of the said array:
#[2, 5, 7, 8, 9, -10, -3, -1]
# Lambda function to rearrange positive and negative numbers
rearrange_numbers = lambda arr: sorted(arr, key=lambda x: (x >= 0, abs(x)))

# Original array
original_array = [-1, 2, -3, 5, 7, 8, 9, -10]

# Rearrange using the lambda function
result = rearrange_numbers(original_array)

# Output
print("Original array:")
print(original_array)
print("\nRearrange positive and negative numbers of the said array:")
print(result)


# In[15]:


#Q.13) Write a Python program to count the even and odd numbers in a given array of integers using Lambda.
#Original arrays:
#[1, 2, 3, 5, 7, 8, 9, 10]
#Number of even numbers in the above array: 3
#Number of odd numbers in the above array: 5

# Lambda function to check if a number is even
is_even = lambda x: x % 2 == 0

# Original array
original_array = [1, 2, 3, 5, 7, 8, 9, 10]

# Counting even and odd numbers using the lambda function
even_numbers_count = len(list(filter(is_even, original_array)))
odd_numbers_count = len(original_array) - even_numbers_count

# Output
print("Original array:")
print(original_array)
print("\nNumber of even numbers in the above array:", even_numbers_count)
print("Number of odd numbers in the above array:", odd_numbers_count)



# In[114]:


#Q.14) Write a Python program to filter a given list to determine if the values in the list have a length of 6 using Lambda.
#Sample Output:
#Monday
#Friday
#Sunday

# Given list
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Use filter and lambda to filter elements with a length of 6
filtered_days = filter(lambda x: len(x) == 6, days_of_week)

# Convert the filter object to a list and print the result
result = list(filtered_days)
print(result)


# In[115]:


#Q.15) Write a Python program to add two given lists using map and lambda.
#Original list:
#[1, 2, 3]
#[4, 5, 6]
#Result: after adding two list
#[5, 7, 9]

# Given lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Use map and lambda to add corresponding elements of the two lists
result = list(map(lambda x, y: x + y, list1, list2))

# Print the result
print("Result after adding two lists:")
print(result)


# In[118]:


#Q.16) Write a Python program to find the second lowest total marks of any student(s) from the given names and marks of each 
#student using lists and lambda. Input the number of students, the names and grades of eachstudent.
#Input number of students: 5
#Name: S ROY
#Grade: 1
#Name: B BOSE
#Grade: 3
#Name: N KAR
#Grade: 2
#Name: C DUTTA
#Grade: 1
#Name: G GHOSH
#Grade: 1
#Names and Grades of all students:
#[['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH',1.0]]
#Second lowest grade: 2.0
#Names:N KAR

# Input number of students
num_students = int(input("Input number of students: "))

# Initialize an empty list to store names and grades
students = []

# Input names and grades of each student
for _ in range(num_students):
    name = input("Name: ")
    grade = float(input("Grade: "))
    students.append([name, grade])

# Print names and grades of all students
print("Names and Grades of all students:")
print(students)

# Use lambda to get unique grades and sort them
unique_grades = sorted(set(grade for name, grade in students))

# Find the second lowest grade
second_lowest_grade = unique_grades[1]

# Find names of students with the second lowest grade
selected_students = list(filter(lambda x: x[1] == second_lowest_grade, students))

# Print the result
print("Second lowest grade:", second_lowest_grade)


# In[1]:


#Q.17) Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
#Orginal list:
#[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
#Numbers of the above list divisible by nineteen or thirteen:
#[19, 65, 57, 39, 152, 190]

# Original list of numbers
numbers = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

# Use filter and lambda to find numbers divisible by nineteen or thirteen
result = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers))

# Print the result
print("Original list:")
print(numbers)
print("Numbers of the above list divisible by nineteen or thirteen:")
print(result)


# In[2]:


#Q.18) Write a Python program to find palindromes in a given list of strings using Lambda.
#Orginal list of strings:
#['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
#List of palindromes:['php', 'aaa']

# Original list of strings
strings = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

# Use filter and lambda to find palindromes
is_palindrome = lambda x: x == x[::-1]
palindromes = list(filter(is_palindrome, strings))

# Print the result
print("Original list of strings:")
print(strings)
print("List of palindromes:")
print(palindromes)


# In[3]:


#Q.19) Write a Python program to find all anagrams of a string in a given list of strings using Lambda.
#Orginal list of strings:['bcda', 'abce', 'cbda', 'cbea', 'adcb']
#Anagrams of 'abcd' in the above string:['bcda', 'cbda', 'adcb']

# Original list of strings
strings = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']

# Given string to find anagrams
given_string = 'abcd'

# Use filter and lambda to find anagrams
is_anagram = lambda x: sorted(x) == sorted(given_string)
anagrams = list(filter(is_anagram, strings))

# Print the result
print("Original list of strings:")
print(strings)
print(f"Anagrams of '{given_string}' in the above strings:")
print(anagrams)


# In[4]:


#Q.20) Write a Python program to find the numbers in a given string and store them in a list. Afterward, display the numbers
#that are longer than the length of the list in sorted form. Use the lambda function to solve the problem.
#Original string: sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5
#Numbers in sorted form:20 23 56

import re

# Original string
original_string = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"

# Use regular expression to find numbers in the string
numbers = re.findall(r'\b\d+\b', original_string)

# Convert the numbers to integers
numbers = list(map(int, numbers))

# Use lambda to filter numbers longer than the length of the list
filtered_numbers = list(filter(lambda x: x > len(numbers), numbers))

# Print the result
print("Original string:", original_string)
print("Numbers in sorted form:")
print(" ".join(map(str, sorted(filtered_numbers))))


# In[5]:


#Q.21) Write a Python program that multiplies each number in a list with a given number using lambda functions. 
#Print the results.
#Original list: [2, 4, 6, 9, 11]
#Given number: 2
#Result:4 8 12 18 22

# Original list of numbers
numbers = [2, 4, 6, 9, 11]

# Given number to multiply
given_number = 2

# Use map and lambda to multiply each number in the list
result = list(map(lambda x: x * given_number, numbers))

# Print the result
print("Original list:", numbers)
print("Given number:", given_number)
print("Result:")
print(" ".join(map(str, result)))




# In[7]:


#Q.22) Write a Python program that sums the length of a list of names after removing those that start with lowercase letters.
#Use the lambda function.
#Result:17

# Original list of names
names = ['John', 'alice', 'Bob', 'Charlie', 'Eva']

# Use lambda and filter to remove names starting with lowercase letters
filtered_names = list(filter(lambda x: not x[0].islower(), names))

# Use lambda and map to get the length of each remaining name
lengths = list(map(lambda x: len(x), filtered_names))

# Calculate and print the sum of lengths
result = sum(lengths)
print("Result:", result)


# In[8]:


#Q.23) Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using 
#the lambda function.
#Original list: [2, 4, -6, -9, 11, -12, 14, -5, 17]
#Sum of the positive numbers: -32
#Sum of the negative numbers: 48

# Original list of numbers
numbers = [2, 4, -6, -9, 11, -12, 14, -5, 17]

# Use lambda and filter to get positive and negative numbers
positive_numbers = list(filter(lambda x: x > 0, numbers))
negative_numbers = list(filter(lambda x: x < 0, numbers))

# Use lambda and sum to calculate the sum of positive and negative numbers
sum_positive = sum(positive_numbers)
sum_negative = sum(negative_numbers)

# Print the result
print("Original list:", numbers)
print("Sum of the positive numbers:", sum_positive)
print("Sum of the negative numbers:", sum_negative)


# In[13]:


#Q.24) Write a Python program to find numbers within a given range where every number is divisible by every digit it contains.

def is_divisible_by_digits(num):
    digits = [int(digit) for digit in str(num) if int(digit) != 0]
    return all(num % digit == 0 for digit in digits)

def find_numbers_in_range(start, end):
    return [num for num in range(start, end + 1) if is_divisible_by_digits(num)]

# Given range
start_range = 1
end_range = 30

# Find numbers within the range
result = find_numbers_in_range(start_range, end_range)

# Print the result
print("Sample Output:")
print(result)


# In[16]:


#Q.25) Write a Python program to create the next bigger number by rearranging the digits of a given number.
#Original number: 12
#Next bigger number: 21
#Original number: 10
#Next bigger number: False
#Original number: 201
#Next bigger number: 210
#Original number: 102
#Next bigger number: 120
#Original number: 445
#Next bigger number: 454

def next_bigger_number(original_number):
    # Convert the number to a list of digits
    digits = list(str(original_number))
    
    # Find the rightmost digit that is smaller than the digit to its right
    for i in range(len(digits) - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            # Find the smallest digit to the right of digits[i] that is larger than digits[i]
            for j in range(len(digits) - 1, i, -1):
                if digits[j] > digits[i]:
                    # Swap digits[i] and digits[j]
                    digits[i], digits[j] = digits[j], digits[i]
                    
                    # Reverse the portion of the list to the right of digits[i]
                    digits[i + 1:] = reversed(digits[i + 1:])
                    
                    # Convert the list of digits back to a number
                    next_number = int("".join(digits))
                    
                    return next_number
    
    return False  # If no next bigger number is possible

# Test cases
test_numbers = [12, 10, 201, 102, 445]

for num in test_numbers:
    result = next_bigger_number(num)
    print(f"Original number: {num}")
    print(f"Next bigger number: {result if result else 'False'}")
    print()


# In[17]:


#Q.26) Write a Python program to find a list with maximum and minimum length using lambda.
#Original list:[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
#List with maximum length of lists:(3, [13, 15, 17])
#List with minimum length of lists:(1, [0])

# Original list of lists
original_list = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

# Use lambda to get the length of each list
length_of_lists = lambda x: len(x)

# Find the list with the maximum length
max_length_list = max(original_list, key=length_of_lists)

# Find the list with the minimum length
min_length_list = min(original_list, key=length_of_lists)

# Print the result
print("Original list:")
print(original_list)
print("List with maximum length of lists:")
print((len(max_length_list), max_length_list))
print("List with minimum length of lists:")
print((len(min_length_list), min_length_list))


# In[18]:


#Q.27) Write a Python program to sort each sublist of strings in a given list of lists using lambda.
#Original list:[['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
#After sorting each sublist of the said list of lists:[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]

# Original list of lists
original_list = [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]

# Use lambda to sort each sublist
sorted_list = [sorted(sublist, key=lambda x: x.lower()) for sublist in original_list]

# Print the result
print("Original list:")
print(original_list)
print("After sorting each sublist of the said list of lists:")
print(sorted_list)


# In[19]:


#Q.28) Write a Python program to sort a given list of lists by length and value using lambda.
#Original list:[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
#Sort the list of lists by length and value:[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]

# Original list of lists
original_list = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]

# Use lambda to sort the list of lists by length and value
sorted_list = sorted(original_list, key=lambda x: (len(x), x))

# Print the result
print("Original list:")
print(original_list)
print("Sort the list of lists by length and value:")
print(sorted_list)


# In[20]:


#Q.29) Write a Python program to find the maximum value in a given heterogeneous list using lambda.
#Original list:['Python', 3, 2, 4, 5, 'version']
#Maximum values in the said list using lambda:5

# Original list
original_list = ['Python', 3, 2, 4, 5, 'version']

# Use lambda to filter numerical values and find the maximum
max_value = max(filter(lambda x: isinstance(x, (int, float)), original_list))

# Print the result
print("Original list:")
print(original_list)
print("Maximum values in the said list using lambda:")
print(max_value)


# In[21]:


#Q.30) Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda.
#Original Matrix:[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
#Sort the said matrix in ascending order according to the sum of its rows :[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
#Original Matrix:[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
#Sort the said matrix in ascending order according to the sum of its rows[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]

# Original matrix
original_matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
original_matrix2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]

# Use lambda to sort the matrix in ascending order according to the sum of its rows
sorted_matrix1 = sorted(original_matrix1, key=lambda x: sum(x))
sorted_matrix2 = sorted(original_matrix2, key=lambda x: sum(x))

# Print the result
print("Original Matrix:")
print(original_matrix1)
print("Sort the matrix in ascending order according to the sum of its rows:")
print(sorted_matrix1)

print("\nOriginal Matrix:")
print(original_matrix2)
print("Sort the matrix in ascending order according to the sum of its rows:")
print(sorted_matrix2)


# In[22]:


#Q.31) Write a Python program to extract a specified size of strings from a given list of string values using lambda.
#Original list:['Python', 'list', 'exercises', 'practice', 'solution']
#length of the string to extract:8
#After extracting strings of specified length from the said list:['practice', 'solution']

# Original list of strings
original_list = ['Python', 'list', 'exercises', 'practice', 'solution']

# Length of the string to extract
specified_length = 8

# Use lambda and filter to extract strings of specified length
result = list(filter(lambda x: len(x) == specified_length, original_list))

# Print the result
print("Original list:")
print(original_list)
print("Length of the string to extract:", specified_length)
print("After extracting strings of specified length from the said list:")
print(result)


# In[23]:


#Q.32) Write a Python program to count float values in a mixed list using lambda.
#Original list:[1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
#Number of floats in the said mixed list:3

# Original mixed list
mixed_list = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]

# Use lambda and filter to count float values
count_floats = len(list(filter(lambda x: isinstance(x, float), mixed_list)))

# Print the result
print("Original list:")
print(mixed_list)
print("Number of floats in the said mixed list:")
print(count_floats)


# In[24]:


#Q.33) Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number 
#and a minimum length using lambda.
#Input the string: W3resource
#['Valid string.']

# Input the string
input_string = input("Input the string: ")

# Use lambda to check the conditions
check_conditions = lambda s: any(c.isupper() for c in s) and any(c.islower() for c in s) and any(c.isdigit() for c in s) and len(s) >= 5

# Check the conditions and print the result
result = ['Valid string.'] if check_conditions(input_string) else ['Invalid string.']
print(result)


# In[25]:


#Q.34) Write a Python program to filter the height and width of students, which are stored in a dictionary using lambda. 
#Original Dictionary:{'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68),'Pierre Cox': (5.8, 66)}
#Height> 6ft and Weight> 70kg:{'Cierra Vega': (6.2, 70)}

# Original Dictionary
student_data = {
    'Cierra Vega': (6.2, 70),
    'Alden Cantrell': (5.9, 65),
    'Kierra Gentry': (6.0, 68),
    'Pierre Cox': (5.8, 66)
}

# Use lambda and filter to filter students based on height and weight
filtered_students = dict(filter(lambda item: item[1][0] > 6.0 and item[1][1] > 70, student_data.items()))

# Print the result
print("Original Dictionary:")
print(student_data)
print("Height > 6ft and Weight > 70kg:")
print(filtered_students)


# In[26]:


#Q.35) Write a Python program to check whether a specified list is sorted or not using lambda.
#Original list:[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
#Is the said list is sorted!
#True
#Original list:[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
#Is the said list is sorted!
#False

# Function to check if a list is sorted
is_sorted = lambda lst: all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

# Original lists
list1 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
list2 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17, 15]

# Check if the lists are sorted
result1 = is_sorted(list1)
result2 = is_sorted(list2)

# Print the results
print("Original list:")
print(list1)
print("Is the said list sorted?")
print(result1)

print("\nOriginal list:")
print(list2)
print("Is the said list sorted?")
print(result2)


# In[27]:


#Q.36) Write a Python program to extract the nth element from a given list of tuples using lambda. Go to the editor
#Original list:[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94),('Beau Turnbull', 94, 98)]
#Extract nth element ( n = 0 ) from the said list of tuples:['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
#Extract nth element ( n = 2 ) from the said list of tuples:[99, 96, 94, 98]

# Original list of tuples
original_list = [
    ('Greyson Fulton', 98, 99),
    ('Brady Kent', 97, 96),
    ('Wyatt Knott', 91, 94),
    ('Beau Turnbull', 94, 98)
]

# Extract nth element (n = 0) using lambda
extracted_n0 = list(map(lambda x: x[0], original_list))

# Extract nth element (n = 2) using lambda
extracted_n2 = list(map(lambda x: x[2], original_list))

# Print the results
print("Original list:")
print(original_list)
print("Extract nth element (n = 0) from the said list of tuples:")
print(extracted_n0)
print("Extract nth element (n = 2) from the said list of tuples:")
print(extracted_n2)


# In[28]:


#Q.37) Write a Python program to sort a list of lists by a given index of the inner list using lambda.
#Original list:[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94),('Beau Turnbull', 94, 98)]
#Sort the said list of lists by a given index ( Index = 0 ) of the inner list
#[('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96), ('Greyson Fulton', 98, 99),('Wyatt Knott', 91, 94)]
#Sort the said list of lists by a given index ( Index = 2 ) of the inner list
#[('Wyatt Knott', 91, 94), ('Brady Kent', 97, 96), ('Beau Turnbull', 94, 98),('Greyson Fulton', 98, 99)]

# Original list of lists
original_list = [
    ('Greyson Fulton', 98, 99),
    ('Brady Kent', 97, 96),
    ('Wyatt Knott', 91, 94),
    ('Beau Turnbull', 94, 98)
]

# Sort the list of lists by a given index (Index = 0) using lambda
sorted_list_index_0 = sorted(original_list, key=lambda x: x[0])

# Sort the list of lists by a given index (Index = 2) using lambda
sorted_list_index_2 = sorted(original_list, key=lambda x: x[2])

# Print the results
print("Original list:")
print(original_list)
print("Sort the said list of lists by a given index (Index = 0) of the inner list:")
print(sorted_list_index_0)
print("Sort the said list of lists by a given index (Index = 2) of the inner list:")
print(sorted_list_index_2)


# In[29]:


#Q.38) Write a Python program to remove all elements from a given list present in another list using lambda.
#Original lists:list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#list2: [2, 4, 6, 8]
#Remove all elements from 'list1' present in 'list2:[1, 3, 5, 7, 9, 10]

# Original lists
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

# Use lambda and filter to remove elements from list1 that are present in list2
result = list(filter(lambda x: x not in list2, list1))

# Print the result
print("Original lists:")
print("list1:", list1)
print("list2:", list2)
print("Remove all elements from 'list1' present in 'list2':")
print(result)


# In[30]:


#Q.39) Write a Python program to find the elements of a given list of strings that contain a specific substring using lambda.
#Original list:['red', 'black', 'white', 'green', 'orange']
#Substring to search:ack
#Elements of the said list that contain specific substring:['black']
#Substring to search:abc
#Elements of the said list that contain specific substring:[]

# Original list of strings
original_list = ['red', 'black', 'white', 'green', 'orange']

# Function to check if a string contains a specific substring
contains_substring = lambda s, substring: substring in s

# Substring to search
substring1 = 'ack'
substring2 = 'abc'

# Use lambda and filter to find elements that contain the specific substring
result1 = list(filter(lambda x: contains_substring(x, substring1), original_list))
result2 = list(filter(lambda x: contains_substring(x, substring2), original_list))

# Print the results
print("Original list:")
print(original_list)
print("Substring to search:", substring1)
print("Elements of the said list that contain the specific substring:")
print(result1)

print("\nSubstring to search:", substring2)
print("Elements of the said list that contain the specific substring:")
print(result2)


# In[31]:


#Q.40) Write a Python program to find the nested list elements, which are present in another list using lambda.
#Original lists: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
#[[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
#Intersection of said nested lists:[[12], [7, 11], [1, 5, 8]]

# Original lists
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
nested_lists = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]

# Use lambda and filter to find the nested list elements present in list1
intersection_result = list(map(lambda nested_list: list(filter(lambda x: x in list1, nested_list)), nested_lists))

# Print the results
print("Original lists:")
print("list1:", list1)
print("Nested lists:", nested_lists)
print("Intersection of said nested lists:")
print(intersection_result)


# In[32]:


#Q.41) Write a Python program to reverse strings in a given list of string values using lambda.
#Original lists:['Red', 'Green', 'Blue', 'White', 'Black']
#Reverse strings of the said given list:['deR', 'neerG', 'eulB', 'etihW', 'kcalB']

# Original list of strings
original_list = ['Red', 'Green', 'Blue', 'White', 'Black']

# Use lambda and map to reverse strings in the given list
reversed_list = list(map(lambda x: x[::-1], original_list))

# Print the results
print("Original list:")
print(original_list)
print("Reverse strings of the said given list:")
print(reversed_list)


# In[33]:


#Q.42) Write a Python program to calculate the product of a given list of numbers using lambda.
#list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Product of the said list numbers:3628800
#list2: [2.2, 4.12, 6.6, 8.1, 8.3]
#Product of the said list numbers:4021.8599520000007

from functools import reduce

# Function to calculate the product of a list of numbers
product = lambda lst: reduce(lambda x, y: x * y, lst)

# List of numbers
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2.2, 4.12, 6.6, 8.1, 8.3]

# Calculate the product of the lists using lambda
result1 = product(list1)
result2 = product(list2)

# Print the results
print("list1:", list1)
print("Product of the said list numbers:", result1)

print("\nlist2:", list2)
print("Product of the said list numbers:", result2)


# In[34]:


#Q.43) Write a Python program to multiply all the numbers in a given list using lambda.
#Original list:[4, 3, 2, 2, -1, 18]
#Multiply all the numbers of the said list: -864
#Original list:[2, 4, 8, 8, 3, 2, 9]
#Mmultiply all the numbers of the said list: 27648

from functools import reduce

# List of numbers
list1 = [4, 3, 2, 2, -1, 18]
list2 = [2, 4, 8, 8, 3, 2, 9]

# Calculate the product of the lists using lambda
result1 = reduce(lambda x, y: x * y, list1)
result2 = reduce(lambda x, y: x * y, list2)

# Print the results
print("Original list:")
print(list1)
print("Multiply all the numbers of the said list:", result1)

print("\nOriginal list:")
print(list2)
print("Multiply all the numbers of the said list:", result2)


# In[35]:


#Q.44) Write a Python program to calculate the average value of the numbers in a given tuple of tuples using lambda.
#Original Tuple:((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
#Average value of the numbers of the said tuple of tuples:(30.5, 34.25, 27.0)
#Original Tuple:((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
#Average value of the numbers of the said tuple of tuples:(25.5, -18.0, 3.75)

# Original tuple of tuples
tuple1 = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
tuple2 = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))

# Calculate the average value using lambda
average1 = tuple(map(lambda *x: sum(x) / len(x), *tuple1))
average2 = tuple(map(lambda *x: sum(x) / len(x), *tuple2))

# Print the results
print("Original Tuple:")
print(tuple1)
print("Average value of the numbers of the said tuple of tuples:")
print(average1)

print("\nOriginal Tuple:")
print(tuple2)
print("Average value of the numbers of the said tuple of tuples:")
print(average2)


# In[36]:


#Q.45) Write a Python program to convert string elements to integers inside a given tuple using lambda.
#Original tuple values: (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
#New tuple values:((233, 33), (1416, 55), (2345, 34))

# Original tuple of tuples with string elements
original_tuple = (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))

# Convert string elements to integers using lambda
converted_tuple = tuple(map(lambda tup: tuple(map(lambda x: int(x) if x.isdigit() else x, tup)), original_tuple))

# Print the results
print("Original tuple values:")
print(original_tuple)
print("New tuple values:")
print(converted_tuple)


# In[37]:


#Q.46) Write a Python program to find the index position and value of the maximum and minimum values in a given list of numbers 
#using lambda.
#Original list:[12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
#Index position and value of the maximum value of the said list:(5, 89)
#Index position and value of the minimum value of the said list:(3, 10.11)

# Original list of numbers
numbers_list = [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]

# Find index position and value of the maximum value using lambda
max_index, max_value = max(enumerate(numbers_list), key=lambda x: x[1])

# Find index position and value of the minimum value using lambda
min_index, min_value = min(enumerate(numbers_list), key=lambda x: x[1])

# Print the results
print("Original list:")
print(numbers_list)
print("Index position and value of the maximum value of the said list:")
print((max_index, max_value))
print("Index position and value of the minimum value of the said list:")
print((min_index, min_value))


# In[38]:


#Q.47) Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be sorted before strings.
#Original list: [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
#Sort the said mixed list of integers and strings:[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']

# Original mixed list of integers and strings
mixed_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]

# Sort the mixed list using lambda
sorted_mixed_list = sorted(mixed_list, key=lambda x: (isinstance(x, int), x))

# Print the results
print("Original list:")
print(mixed_list)
print("Sort the said mixed list of integers and strings:")
print(sorted_mixed_list)


# In[39]:


#Q.48) Write a Python program to sort a given list of strings (numbers) numerically using lambda.
#Original list:['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
#Sort the said list of strings(numbers) numerically:['-500', '-12', '0', '4', '7', '12', '45', '100', '200']

# Original list of strings (numbers)
string_numbers_list = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']

# Sort the list numerically using lambda
sorted_numbers_list = sorted(string_numbers_list, key=lambda x: int(x))

# Print the results
print("Original list:")
print(string_numbers_list)
print("Sort the said list of strings (numbers) numerically:")
print(sorted_numbers_list)


# In[40]:


#Q.49) Write a Python program to count the occurrences of items in a given list using lambda.
#Original list: [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
#Count the occurrences of the items in the said list:{3: 4, 4: 2, 5: 3, 8: 2, 0: 2, 1: 1, 2: 2}

from collections import Counter

# Original list
original_list = [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]

# Count the occurrences of items using lambda and Counter
occurrences = dict(Counter(original_list))

# Print the results
print("Original list:")
print(original_list)
print("Count the occurrences of the items in the said list:")
print(occurrences)


# In[41]:


#Q.50) Write a Python program to remove specific words from a given list usinglambda.
#Original list:['orange', 'red', 'green', 'blue', 'white', 'black']
#Remove words:['orange', 'black']
#After removing the specified words from the said list:['red', 'green', 'blue', 'white']

# Original list
original_list = ['orange', 'red', 'green', 'blue', 'white', 'black']

# Words to remove
words_to_remove = ['orange', 'black']

# Remove specified words using lambda and filter
filtered_list = list(filter(lambda x: x not in words_to_remove, original_list))

# Print the results
print("Original list:")
print(original_list)
print("Remove words:")
print(words_to_remove)
print("After removing the specified words from the said list:")
print(filtered_list)


# In[42]:


#Q.51) Write a Python program to find the maximum and minimum values in a given list of tuples using the lambda function.
#Original list with tuples:[('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
#Maximum and minimum values of the said list of tuples:(74, 62)

# Original list of tuples
list_of_tuples = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]

# Find maximum and minimum values using lambda
max_tuple = max(list_of_tuples, key=lambda x: x[1])
min_tuple = min(list_of_tuples, key=lambda x: x[1])

# Print the results
print("Original list with tuples:")
print(list_of_tuples)
print("Maximum and minimum values of the said list of tuples:")
print(max_tuple[1], min_tuple[1])


# In[43]:


#Q.52) Write a Python program to remove None values from a given list using the lambda function.
#Original list:[12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
#Remove None value from the said list:[12, 0, 23, -55, 234, 89, 0, 6, -12]

# Original list
original_list = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]

# Remove None values using lambda and filter
filtered_list = list(filter(lambda x: x is not None, original_list))

# Print the results
print("Original list:")
print(original_list)
print("Remove None value from the said list:")
print(filtered_list)


# In[ ]:




