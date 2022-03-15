import csv

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

print()

def main():
    print('Inkom Emporium')
    
    products_dict = read_dict('products.csv', 0)
    # print(products_dict)
    
    with open('request.csv', 'r') as file:
        csvreader = csv.reader(file)
        next (csvreader) #this skips first line in the csv file

        subtotal = 0
        num_of_items = 0
        sales_tax = 0

        print()
        print('Requested Items')
        for row in csvreader:
            num = row[0]
            quantity = int(row[1])
            products = products_dict[num]
            name = products[1]
            price = products[2]
            price = float(price)

            num_of_items += quantity
            subtotal += price * quantity
            sales_tax = 0.06 * subtotal
            total = subtotal + sales_tax

            print(f'{name}: {quantity} @ {price}')

        print()
        print(f"Substotal: ${subtotal:.2f}")
        print(f"Number of items: {num_of_items}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: ${total:.2f}")

        

    # Call the now() method to get the current
    # date and time as a datetime object from
    # the computer's operating system.
    current_date_and_time = datetime.now()

    # Print the current day of the week and the current time.
    print()
    print(f"{current_date_and_time:%A %I:%M %p}")



def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    csvdict = {}
    with open(filename) as file:
        csvreader = csv.reader(file)
        next(csvreader) #this skips first line in the csv file
        
        for row in csvreader:
            key = row[0]
            csvdict[key]= row
    return csvdict

main()


print()