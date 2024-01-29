def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    gallons_consumed = miles_driven / miles_per_gallon
    cost = gallons_consumed * dollars_per_gallon
    return cost
def main():
    mpg = 20.0
    price = 3.1599
    distances = [10, 50, 400]
    for distance in distances:
        cost = driving_cost(mpg, price, distance)
        print(f'{cost:.2f}')

if __name__ == '__main__':
    main()