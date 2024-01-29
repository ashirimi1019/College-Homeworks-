# Prolog (3 P's)
# Author: Ashir Imran
# Email: aimran6@student.gsu.edu
# Section: 030
#'''
# -Purpose
#   The purpose is to see if any given number is a prime number or not.
# -Precondition
#  Input Integer that you want to check if it's prime or not
# -Postcondition
# - Calculate if the integer has factors or not and if it's negative or not.

import math
def isprime():
# Displaying Intro Message.
     print()
number = int(input("Enter a Integer: "))

# If number is greater than 1
if number > 1:
   # Check if factor exist  
   for i in range(2,number):
       if (number % i) == 0:
           print(number,"is a prime number")
           break
   else:
       print(number,"is a prime number")
       
# Else if the input number is less than or equal to 1
else:
   print(number,"is a negative")

   isprime()


