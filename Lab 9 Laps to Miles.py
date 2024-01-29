# Prolog
# Author: Ashir Imran
# Email: aimran6@gsu.edu
# Section: 030
#Define your function here
from datetime import datetime 
 
def laps_to_miles(user_laps):
    return user_laps*0.25
    
laps=float(input("enter user_laps: "))
miles=laps_to_miles(laps)
print(f'{miles:.2f}')

