# accounts.py
# This program will read in a bank account number of any length
# and output the number where only the last 4 digits are shown
# and all the other digits are replaced with 'X's
# Author: Zoe McNamara Harlowe

# I casted the input number to a string to allow for easier manipulation of the number
raw_account_number = str(input("Please enter your bank account number: "))

# I then isolated the last 4 digits
last_four_digits = (raw_account_number[-4:])

# I then replaced all the other digits with 'X's using the replace() method
'''
hidden_account_number = raw_account_number.replace(raw_account_number[:-4], 'X')
print(hidden_account_number)
'''
# The output only gave me one 'X' 
# I realised I had to use the len() function to output the correct number of 'X's
hidden_account_number = raw_account_number.replace(raw_account_number[:-4], 'X' * len(raw_account_number[:-4]))
print(hidden_account_number)