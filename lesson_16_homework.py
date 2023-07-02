#Exception Handling

class InvalidInputError(Exception):
    pass

def calculate_division():
    try:
        num1 = input("Enter the first number: ")
        num1 = int(num1)
        num2 = input("Enter the second number: ")
        num2 = int(num2)

        result = num1/num2
        print(result)
    except ZeroDivisionError:
        print("Division by zero is not allowed. Please re-enter the second number.")
    except ValueError:
        raise InvalidInputError ("Invalid input. Please enter integers only.")

try:        
    calculate_division() 
except InvalidInputError as e:
    print(e)


#Pytest 

import pytest

def get_sum(num1, num2):
    return num1 + num2

def test_sum():
    assert get_sum(2,6) == 8
    assert get_sum(-5, 10) == 5
    assert get_sum(0,0) == 0

      

