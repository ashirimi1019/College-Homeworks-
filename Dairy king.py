# Prolog
# Author: Ashir Imran
# Email: aimran6@gsu.edu
# Section: 030
from datetime import datetime 
def DairyKing():
    # Design and implementation
    grilledcheese = 7.00
    nachos = 5.00
    chicken = 8.00
    hamburger = 8.00
    cheeseburger = 10.00
    hotdog = 6.00
    total = 0.00
    print()
    print("Welcome to Dairy King!")
    print("Please answer each question with y or n")
    grilledcheeseselection = input("Do you want a grilled cheese sandwich? ")
    if grilledcheeseselection == 'y':
        total = total + 7.00
    nachosselection = input("Do you want a serving of nachos? ")
    if nachosselection == 'y':
        total = total + 5.00
    chickenselection = input("Do you want a chicken sandwich? ")
    if chickenselection == 'y':
        total = total + 8.00
    hamburgerselection = input("Do you want a hamburger? ")
    if hamburgerselection == 'y':
        total = total + 8.00
        cheeseburgerselection = input("Do you want cheese on that? ")
        if cheeseburgerselection == 'y':
            total = total + 2.00
    else: next
    hotdogselection = input("Do you want a hotdog? ")
    if hotdogselection == 'y':
        total = total + 6.00
    totalwithtip = 1.20*total
    totalwithtip = '%.2f' % totalwithtip
    print("The total for your food is $",total)
    print("The total with 20% tip is $",totalwithtip)
    print("Thank you for your business!")
    dt = datetime.now()
    print("Date and time is: ", dt)
DairyKing()
