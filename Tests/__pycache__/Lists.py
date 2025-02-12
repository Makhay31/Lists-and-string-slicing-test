from typing import List, Optional, Dict

# Part 1: List Operations
numbers = [] #Global variable that is changed in multiple functions
def create_numbers_list():
    """
    1.  Create a list named `numbers` containing the integers from 1 to 10 (inclusive).
        Return the numbers list
    """
    for number in range(1,11):
        numbers.append(number)
    return numbers

def add_eleven(numbers_list): # Modified to accept numbers_list as argument
    """
    2.  Add the number 11 to the end of the `numbers_list`.
    """
    #pass # Replace with your code
    numbers.append(11)
    numbers_list = numbers
    return numbers_list

def insert_zero(numbers_list): # Modified to accept numbers_list as argument
    """
    3.  Insert the number 0 at the beginning of the `numbers_list`.
    """
    #pass # Replace with your code
    numbers.insert(0,0)
    numbers_list = numbers
    return numbers_list

def remove_five(numbers_list): # Modified to accept numbers_list as argument
    """
    4.  Remove the number 5 from the `numbers_list`. (Remove the *value* 5, not the element at index 5).
    """
    #pass # Replace with your code
    for number in numbers:
        if number == 5:
            numbers.pop(numbers.index(5))
    numbers_list = numbers
    return numbers_list


# Part 2: List Comprehension

def create_even_numbers(numbers_list): # Modified to accept numbers_list as argument
    """
    1.  Using list comprehension, create a new list named `even_numbers` containing only the even numbers
        from the `numbers_list` (created/modified in Part 1).
        Return even_numbers
    """
    #return None #Replace with your code
    even_numbers = []
    for number in numbers :
        if number % 2 == 0:
            even_numbers.append(number)
    numbers_list = numbers
    return numbers_list

def create_squared_numbers(numbers_list): # Modified to accept numbers_list as argument
    """
    2.  Using list comprehension, create a new list named `squared_numbers` containing the square of each number in
        the `numbers_list`. Return squared_numbers
    """
    #return None #Replace with your code
    squared_numbers =[]
    for number in numbers:
        squared_numbers.append(number**2)
    numbers_list = numbers
    return numbers_list

# Part 3: String Slicing
def extract_hello(text):
    """
    1.  Given the string `text = "Hello, World!"`, extract the substring "Hello".
        Return the string.
    """
    #return None #Replace with your code
    return text[0:5]

def extract_world(text):
    """
    2.  Given the string `text = "Hello, World!"`, extract the substring "World".
        Return the string
    """
    #return None #Replace with your code
    return text[7:12]

def reverse_string(text):
    """
    3.  Given the string `text = "Hello, World!"`, create a new string that is the reversed version of the original string.
        Return the reversed string
    """
    #return None #Replace with your code
    return text[::-1]

#Part 4: More list operations

def get_second_element(my_list):
    """
    1. Given a list called my_list, return the second element in the list, or None if it doesn't exist
    """
    if len(my_list) >= 2:
        return my_list[1]
    else:
        return None #Replace with your code

def get_last_three_elements(my_list):
    """
    2. Given a list called my_list, return a new list consisting of the last three elements in my_list.
    If there are fewer than three elements, return a list with the elements that there are
    """
    threes =list(my_list[len(my_list)-1:len(my_list)-4:-1])
    if len(my_list) >= 3:
        return threes
    else:
        return my_list
        
        
    #return None #Replace with your code

def replace_element(my_list, index, new_value):
    """
    3. Given a list called my_list, an integer index, and a new value, replace the element
       at the given index in my_list with the new value. Assume the list is valid
    """
    my_list[index] == new_value
    return my_list
    #pass #Replace with your code