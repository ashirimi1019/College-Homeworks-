# Prolog
# Author: Ashir Imran
# Email: aimran6@gsu.edu
# Section: 030
from datetime import datetime
def driving_cost(mpg, dpg,):
    #Calculate the gas cost for a given number of miles driven.
    cost_per_mile = dpg / mpg
    return cost_per_mile * 10, cost_per_mile * 50, cost_per_mile * 400
def main():
    mpg = float(input("car's miles per gallon: "))
    dpg = float(input("price of gas in dollars per gallon: "))
# Call the driving_cost() function with different miles driven
    cost_10, cost_50, cost_400 = driving_cost(mpg, dpg,)
# Output the gas cost for 10 miles, 50 miles, and 400 miles
    print(f' cost for 10 miles: {cost_10:.2f}')
    print(f' cost for 50 miles: {cost_50:.2f}')
    print(f' cost for 400 miles: {cost_400:.2f}')
    dt = datetime.now()
    print("Date and time is: ", dt)
main()