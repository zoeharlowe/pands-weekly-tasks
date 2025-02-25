# collatz.py
# This program reads in a positive integer
# If the integer is even, it divides it by two
# If it is odd, it multiplies it by three and adds one
# The program will stop once it outputs the number 1
# Author: Zoe McNamara Harlowe

# First, I initialise the number variable to the user's input
# I create a list called numbers and add the user's input to it
number = (int(input("Please enter a positive integer: ")))
numbers = [number,]

# I create a while loop that will run until the number is equal to 1

while number != 1:
    # I put an if statement inside the while loop to determine if the number is even or odd
    if number % 2 == 0:
        number = number // 2
        # All numbers that the Collatz conjecture produces are appended to the numbers list
        numbers.append(number)
    else:
        number = number * 3 + 1
        numbers.append(number)

# I print out the numbers in the list using the * operator to unpack the list and remove brackets
print(*numbers) 
