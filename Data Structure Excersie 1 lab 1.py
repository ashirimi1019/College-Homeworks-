#NAME:Ashir Imran
#DATA STRUCTURE lab 1
#Date: 1/10/2024
def personalized_hello_world():
    while True:
        # Prompt user for their name
        print("What is your name?")
        user_input = input("Please enter your name: ")

        # Check if the user entered anything
        if user_input.strip() != "":
            # Display personalized greeting
            print("Hello, {}!".format(user_input))
            break
        else:
            # If user didn't enter anything, reprompt
            print("Please enter your name:")

# Run the program
personalized_hello_world()

