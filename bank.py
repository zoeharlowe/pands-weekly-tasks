# bank.py
# This program reads in two money amounts, adds them and prints the result in a readable format
# Author: Zoe McNamara Harlowe

# First I got the program to output the sum of the two amounts in cent
money1 = int(input("Enter the first amount (in cent): "))
money2 = int(input("Enter the second amount (in cent): "))
total = ((money1) + (money2))


# Then I got the program to output the total in euro

euro = total / 100
print(euro)

# I had to play around with it a lot to figure out how to print the strings with the numbers

'''
print("The total amount is €" + euro)
'''
# I learned how to convert a float to a string on this website: https://bobbyhadz.com/blog/python-typeerror-can-only-concatenate-str-not-int-to-str#typeerror-can-only-concatenate-str-not-float-to-str

finalAmount = str(euro)
print("The total amount is €" + finalAmount)

