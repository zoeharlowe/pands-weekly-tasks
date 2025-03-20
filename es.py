# es.py
# This program will output how many times it counts the letter 'e' in a text file
# The file will be passed in as an argument on the command line
# Author: Zoe McNamara Harlowe


# Import os module to deal with the error of the filename not existing
import os

# Import sys module to pass filename in as argument on command line
import sys

# The text file I'm mainly using to test this program is 'sample.txt'.
FILENAME = sys.argv[1]

# Function e_count()
def e_count():

    # Set count as 0
    count = 0

    # Open the file in read mode
    with open(FILENAME, "rt") as f:

        # For loop to count instances of letter e or E
        for line in f:

            # I am going to count all instances of e, both capital and lower-case
            count += line.count("e")
            count += line.count("E")

        print(count)


# Error handling
try: 
    e_count()

except FileNotFoundError:
    print(f"{FILENAME} not found")
    sys.exit(1)

