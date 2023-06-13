##Task 1: Create a closure function called calculator that performs basic arithmetic operations. The closure should return a function that takes two numbers and performs a specified operation on them.

def calculator():
    def operate(num1, num2, operation):
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            return num1 / num2
        else:
            raise ValueError("Invalid operation")
    return operate

#Create a calculator instance by calling the calculator() function
cal = calculator()

print(cal(6,3,"add"))
print(cal(6,3,"divide"))
#print(cal(5,3,"power"))




## Task 2: Decorators - Timer

import time 
def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        execute_time = end_time - start_time
        print(execute_time)
    return wrapper

@timer
def myfunc():
    time.sleep(3)
    print("Function is complete.")
myfunc()



##Task 3: Special Methods

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        return False

rectangle = Rectangle(5,6)

print(str(rectangle))

rectangle1 = Rectangle(6,3)
rectangle2 = Rectangle(6,3)
rectangle3 = Rectangle(5,8)


print(rectangle1 == rectangle2)
print(rectangle1 == rectangle3)