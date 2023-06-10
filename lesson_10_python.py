# Write a Python program that reads a text file called "input.txt" and counts the occurrences of each word in the file. Print the word and its count. Ignore case sensitivity (treat "Hello" and "hello" as the same word).

import string

# Open the file in read mode
file = open("input.txt","r")
# Create an empty dictionary
d = dict()

# Loop through each line of the file
for line in file:
    # Convert the characters to lower case to avoid mismatch
    line = line.lower()
    # Remove the punctuation marks from the line
    line = line.translate(line.maketrans("", "", string.punctuation))
    # Split the line into each word
    words = line.split(" ")
# Iterate over each word in the list of words 
for word in words:
    # Check if the word is already in dictionary
    if word in d:   
        # Increment count of word by 1
        d[word] += 1
    else:
        # Add the word to dictionary with count 1
        d[word] = 1

# Iterate each key in the dictionary        
for key in list(d.keys()):
       # Print the key and its corresponding value
       print(key,": ", d[key]) 
   



#Write a Python lambda function that takes two parameters a and b, and returns the sum of their squares. Assign the lambda function to a variable called sum_of_squares. Test the lambda function by passing different values for a and b.



sum_of_squares = lambda a, b: a**2 + b**2

print(sum_of_squares(5,8))
print(sum_of_squares(10,20))



# Write a Python function called calculate_average that accepts a variable number of arguments (numbers) and returns the average of those numbers. Test the function with different sets of numbers.

def calculate_average(*args):
     # find the length of arguments 
     if len(args) ==0:
          return 0
     
     total = sum(args)
     average = total/ len(args)
     return average


print(calculate_average(1,2,3))

