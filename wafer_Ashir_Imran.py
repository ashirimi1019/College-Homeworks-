# Prolog (3 P's)
# Author: Ashir Imran
# Email: aimran6@student.gsu.edu
# Section: 050
#'''
# -Purpose
#   The purpose is to see how many Dies can produced from one or more wafers.
# -Precondition
#   input Diameter of wafer and area of one die.
# -Postcondition
# - Calculate the amount of dies which can be cut fron wafer area.

# main function
import math
def main():
# Displaying Intro Message.
     print()
print("Please Wait While we slice The Wafers")
print()
wafer_diameter = float(input("Enter the diameter of the wafer.(mm)"))
dies_area = float(input("Enter the area of the single die.(mm^2)"))
print()

wafer_area = round((math.pi * (wafer_diameter / 2) ** 2), 2)

dies_per_wafer = int((wafer_area / dies_area) - ((math.pi * wafer_diameter) / (math.sqrt(2 * dies_area))))

print("From a wafer with area",wafer_area,"square millimeters")
print("you can cut" ,dies_per_wafer, "dies.")
print("This does not take into account defective dies, alignment markings and test")
print("sites on the wafer's surface.")
