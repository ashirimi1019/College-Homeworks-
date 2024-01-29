from datetime import datetime 
def main():
    num = float(input("Write any number: "))
    if num>0:
        print("Positive")
    if num==0:
        print("Neither positive nor negative")
    if num<0:
        print("Negative")
main()
from datetime import datetime
def main():
    # User inputs X and O
    row1=str(input(("ROW 1> ")))
    row2=str(input(("ROW 2> ")))
    row3=str(input(("ROW 3> ")))
    # Print the resulting board
    print("ROW1>",row1)
    print("ROW2>",row2)
    print("ROW3>",row3)
    # Set all to false
    horizontal = False
    vertical = False
    diagonal = False
    # Determine if horizontal in X or O
    if row1[0]==row1[1]==row1[2]=='X' or row2[0]==row2[1]==row2[2]=='X' or row3[0]==row3[1]==row3[2]=='X':
        horizontal = True
        print("X IS GOOD IN HORIZONTAL")
    if row1[0]==row1[1]==row1[2]=='O' or row2[0]==row2[1]==row2[2]=='O' or row3[0]==row3[1]==row3[2]=='O':
        horizontal = True
        print("O IS GOOD IN HORIZONTAL")
    # Determine if horizontal in X or O
    if row1[0]==row2[0]==row3[0]=='X' or row1[1]==row2[1]==row3[1]=='X' or row1[2]==row2[2]==row3[2]=='X':
        vertical = True
        print("X IS GOOD IN VERTICAL")
    if row1[0]==row2[0]==row3[0]=='O' or row1[1]==row2[1]==row3[1]=='O' or row1[2]==row2[2]==row3[2]=='O':
        vertical = True
        print("O IS GOOD IN VERTICAL")
    # Determine if diagonal in X or O
    if row1[0]==row2[1]==row3[2]=='X' or row1[2]==row2[1]==row3[0]=='X':
        diagonal = True
        print("X IS GOOD IN DIAGONAL")
    if row1[0]==row2[1]==row3[2]=='O' or row1[2]==row2[1]==row3[0]=='O':
        diagonal = True
        print("O IS GOOD IN DIAGONAL")
    # Determine if a tie
    if diagonal==False and horizontal==False and vertical==False:
        print("THIS IS A TIE")
    dt = datetime.now()
    print("Date and time is: ", dt)
main()
