
'''
Purpose:
convert celsuis to fahrenheit.
Pre-conditions (input):
number of inches (floating point)
Post-conditions (output):
number of feet, floating point with 2 decimals rounded
'''
def main():
    # Design and implementation
    # 1. Output a message to identify the program, and a blank line
    print("Conversion of Celsius to Fahrenheit.")

    # 2. Input Celsius temperature from user
    Celsius = float(input("Enter temperature in Celsius: "))

    # 3. Calculate Fahrenheit
    Fahrenheit = (Celsius * 1.8) + 32

    # 4. Output resulting Celsius and corresponding Fahrenheit
    print()
    print(f"{Celsius} degree Celsius is equal to {Fahrenheit} degree Fahrenheit.")

if __name__ == "__main__":
    main()
