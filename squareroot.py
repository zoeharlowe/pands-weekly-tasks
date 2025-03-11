# squareroot.py
# This program takes a positive float as input and outputs it's square root (approx.)
# Author: Zoe McNamara Harlowe

# I've blocked out my attempt at the code below as I couldn't get it to work
# Underneath is an answer given to me by Galaxy AI Code Generator that I slightly modified

'''
# Import random module to pick a new number to be the variable each time
import random 

def sqrt(num):
    # Choose a random number to be the variable in the algorithm
    # I used random.triangular to ensure that floats would be accepted
    new_variable = 0
    new_val = 0
    variable = random.triangular(0, num)
    val = num / variable
    if variable != val: 
        # If statement to choose a new number to estimate with depending on which one was greater, val or variable
        if variable < val:
            # If variable is greater than val, I need to try again with a bigger number
            new_variable = random.triangular(0, variable)
        else: 
            # If val is greater than variable, I need to try again with a smaller number
            new_variable = random.triangular(0, variable)
        new_val = num / new_variable
        new_variable = (variable + new_val) / 2
        while new_variable != new_val:
            if new_variable < new_val:
            # If variable is greater than val, I need to try again with a bigger number
                new_variable = random.triangular(0, new_variable)
            else: 
            # If val is greater than variable, I need to try again with a smaller number
                new_variable = random.triangular(0, new_variable)
            new_val = num / new_variable
            new_variable = (variable + new_val) / 2
        print("The square root is", new_variable)
    return num

# User inputs positive float
num = float(input("Please enter a positive number: "))
sqrt(num)
'''

def sqrt(number, tolerance=1e-10, max_iterations=1000):

    #Calculate the square root of a given number using Newton's method.

    # Parameters:
    # number (float): The number to find the square root of. Must be non-negative.
    # tolerance (float): The acceptable error margin for the result. Default is 1e-10.
    # max_iterations (int): The maximum number of iterations to perform. Default is 1000.

    # Returns:
    # float: The estimated square root of the number.

    # Raises:
    # ValueError: If the input number is negative.
    
    if number < 0:
        raise ValueError("Cannot compute square root of a negative number.")

    # Initial guess for the square root
    guess = number / 2.0

    for iteration in range(max_iterations):
        # Calculate a new guess using Newton's formula
        new_guess = (guess + number / guess) / 2.0
        
        # Check if the absolute difference is within the tolerance
        if abs(new_guess - guess) < tolerance:
            return new_guess
        
        # Update the guess for the next iteration
        guess = new_guess

    # If we reach here, we didn't converge within the maximum iterations
    raise RuntimeError("Failed to converge to a solution within the maximum number of iterations.")


# Usage of the sqrt function
try:
    input_number = float(input("Enter a non-negative floating-point number: "))
    result = sqrt(input_number)
    print(f"The square root of {input_number} is approximately {result}.")
except ValueError as ve:
    print(ve)
except RuntimeError as re:
    print(re)    