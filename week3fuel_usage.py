'''Week 3'''

print()
mpg = 0
# use function
def main():
     # Get an odometer value in U.S. miles from the user.
    start = float(input("Enter starting odometer in miles: "))
    # Get another odometer value in U.S. miles from the user.
    end = float(input("Enter ending odometer in miles: "))
    # Get a fuel amount in U.S. gallons from the user.
    gal = float(input("Enter fuel amount in gallons: "))
    
    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_pg(start, end, gal)

    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)
    
    # Display the results for the user to see.
    print()
    print(f'{mpg:.2f} miles per gallon')
    print(f'{lp100k:.2f} liters per 100 kilometers')
    print()

def miles_pg(start, end, gal):
    mpg = (end - start) / gal
    return mpg

def lp100k_from_mpg(mpg):
    lpk100k = 235.215 / mpg
    return lpk100k


main()