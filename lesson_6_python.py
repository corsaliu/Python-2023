## Scope and namespace 

def calculate_price(quantity, price):
    # local scope
    total_price = quantity*price
    discount = 0.1

    def apply_discount(price):
        # local scope
        return price*(1-discount)

    return apply_discount(total_price)

# global scope
print(calculate_price(5,10))



## Decorators

import time

def timeit(func):
    def wrappers():
        start_time = time.time()
        func()
        end_time = time.time()
        execution_time = end_time - start_time
        print(execution_time)
    return wrappers


@timeit
def complex_calculation():
    time.sleep(3)


@timeit
def print_stuff():
    print('hello world')


complex_calculation()

print_stuff()





## Best practices

def sum_even(numbers):
    """
    Calculate the sum of all even numbers in a given list of integers.
    
    Arguments:
    numbers - a list of numbers to sum

    Returns:
    the sum of the even numbers in the list
    """
    total_sum = 0 
    for num in numbers:
        if num % 2 == 0:
            total_sum += num
    return total_sum 

print(sum_even([1,5,10,6,13,22]))