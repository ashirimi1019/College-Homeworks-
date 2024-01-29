# Prolog
# Author: Ashir Imran
# Email: aimran6@gsu.edu
# Section: 030
'''
Purpose:
convert inches to feet, using fact that there are 12 inches in 1 foot
Pre-conditions (input):
number of inches (floating point)
Post-conditions (output):
number of feet, floating point with 2 decimals rounded
'''
def main():
# Design and implementation
# 1. Output a message to identify the program, and a blank line
 print("Conversion of inches to feet")
# 2. Input amount of inches from user
inches = float(input("How many inches? "))
# 3. Calculate number of feet
# 12 inches in one foot
feet = inches/12;
# 4. Output resulting feet and given number of inches
print()
print(inches," inches is {:.2f} feet".format(feet))
main()
# end of program file
#

#Line:13 Indent Error Fixed by Putting Indent.
#Line:16 Expected indent error fixed by pressing space beofre print and leaving one space.
#line:19 Removed Int that caused syntax error.
#line:22 Removed The asterisk
#line:22 Changed to inches/12*1
#line:26 Removed colon
