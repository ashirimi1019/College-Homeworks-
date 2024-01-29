# Prolog
# Author: Ashir Imran
# Email: aimran6@gsu.edu
# Section: 030
from datetime import datetime 
def makelist(n):
        # Design and implementation
    li=[]
    for i in range(n):
        li.append(i)
    return li
def rocketcountdown(n):
    li=[]
    for i in range(n,0,-1):
        li.append(i)
    li.append('We have lift off!')
    return li
def doubleLoop(a,b):
    li=[]
    for i in range(a):
        for j in range(b):
            li.append('{}:{}'.format(i,j))
    return li
print(makelist(10))
print(rocketcountdown(10))
print(doubleLoop(3,4))
dt = datetime.now()
print("Date and time is: ", dt)