def get_currency(change, value):
    if change//value > 0:
        bills = change//value
        change -= bills * value
        return bills, change
    else:
        return 0, change

cost = float(input('Cost: '))
paid = float(input('Amount Paid: '))
while paid < cost:
    paid = float(input('Amount Paid: '))

change = paid - cost

hundreds, change, = get_currency(change, 100)

fifties, change, = get_currency(change, 50)

twenties, change = get_currency(change, 20) 

tens, change = get_currency(change, 10) 

fives, change = get_currency(change, 5)

ones, change = get_currency(change, 1)

quarters, change = get_currency(change, .25)

dimes, change = get_currency(change, .1) 

nickels, change = get_currency(change, .05)

pennies = round(change * 100)

print(f"Hundreds: {hundreds}, Fifties: {fifties}, Twenties: {twenties}," +
      f" Tens: {tens}, Fives: {fives}, Ones: {ones}, Quarters: {quarters}," +  
      f" Dimes: {dimes}, Nickels: {nickels}, Pennies: " +
      f"{pennies}")