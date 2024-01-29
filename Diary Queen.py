from datetime import datetime 
def DairyKing():
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
    grilledcheesechoice = input("Do you want a grilled cheese sandwich? ")
    if grilledcheesechoice == 'y':
        total = total + 7.00
    nachoschoice = input("Do you want a serving of nachos? ")
    if nachoschoice == 'y':
        total = total + 5.00
    chickenchoice = input("Do you want a chicken sandwich? ")
    if chickenchoice == 'y':
        total = total + 8.00
    hamburgerchoice = input("Do you want a hamburger? ")
    if hamburgerchoice == 'y':
        total = total + 8.00
        cheeseburgerchoice = input("Do you want cheese on that? ")
        if cheeseburgerchoice == 'y':
            total = total + 2.00
    else: next
    hotdogchoice = input("Do you want a hotdog? ")
    if hotdogchoice == 'y':
        total = total + 6.00
    totalwithtip = 1.20*total
    totalwithtip = '%.2f' % totalwithtip
    print("The total for your food is $",total)
    print("The total with 20% tip is $",totalwithtip)
    print("Thank you for your business!")
    dt = datetime.now()
    print("Date and time is: ", dt)
DairyKing()
