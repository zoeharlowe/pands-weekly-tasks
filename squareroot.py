# squareroot.py
# This program takes a positive float as input 
# and outputs an approximation of its square root
# Author: Zoe McNamara Harlowe

# I am going to recreate the Newton method of estimating square roots in this function
# In the Newton method, 

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
            