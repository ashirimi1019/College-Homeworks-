# Prolog
# Author: Ashir Imran
# Email: aimran6@gsu.edu
# Section: 030
'''
 Purpose:
 calculate the change you are due when you buy an item in a store
 Pre-conditions (input):
 money given to the cashier(cost of item)
 Post-conditions (output):
change user get back from the cashier(dollars, quarters, dimes, nickels and
pennies)
'''
def get_currency(change, value):
# Design and implementation
# 1. Output a message to identify the program, and a blank line
 if change//value > 0:
        bills = change//value
        change -= bills * value
        return bills, change
 else:
        return 0, change
# 2. Input amount of change from user
cost = float(input('Cost: '))
paid = float(input('Amount Paid: '))
while paid < cost:
    paid = float(input('Amount Paid: '))
# 3. Calculate the change
change = paid - cost

hundreds, change, = get_currency(change, 100)

fifties, change, = get_currency(change, 50)

twenties, change = get_currency(change, 20) 

tens, change = get_currency(change, 10) 

fives, change = get_currency(change, 5)

ones, change = get_currency(change, 1)

quarters, change = get_currency(change, .25)

dimes, change = get_currency(change, .1) 

nickels, change = get_currency(change, .05)

pennies = round(change * 100)

print(f"Hundreds: {hundreds}, Fifties: {fifties}, Twenties: {twenties}," +
      f" Tens: {tens}, Fives: {fives}, Ones: {ones}, Quarters: {quarters}," +  
      f" Dimes: {dimes}, Nickels: {nickels}, Pennies: " +
      f"{pennies}")
 

# 4. Output resulting change and given cost of an item

# end of program file

# CHANGES MADE.
#[ln 17, Col 1] paranthesis was not closed properly i fixed it by putting the contents of line 18 into line 17.
# In line 20 wrong quotation marks were used.
# assigned values to each term for example like pennies and nickels.
# Assigned a better fuction to make code work better.
# I could not the values to say the term dollars but Professor Dinesh said it's fine when it was shown to him.
