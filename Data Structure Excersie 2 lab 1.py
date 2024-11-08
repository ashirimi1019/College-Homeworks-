#NAME:Ashir Imran
#DATA STRUCTURE lab 1
#Date: 1/10/2024
import math
def guess_my_number():
    # Get a positive integer n from the user
    while True:
        try:
            n = int(input("Enter n: "))
            if n <= 0:
                raise ValueError("Please enter a positive integer for n.")
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    print("Welcome to Guess My Number!")
    print("Please think of a number between 0 and {}.".format(n - 1))

    # Initialize the range for guessing
    low = 0
    high = n - 1

    # Continue guessing until correct
    while low <= high:
        # Make a guess using the divide-and-conquer algorithm
        guess = math.ceil((low + high) / 2)

        # Ask the user if the guess is correct, too high, or too low
        response = input("Is your number: {}?\nPlease enter C for correct, H for too high, or L for too low.\nEnter your response (H/L/C): ".format(guess))

        if response.upper() == "C":
            print("Thank you for playing Guess My Number!")
            break
        elif response.upper() == "H":
            high = guess - 1
        elif response.upper() == "L":
            low = guess + 1
        else:
            print("Invalid response. Please enter H, L, or C.")

# Run the program
guess_my_number()


