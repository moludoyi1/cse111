import csv

print()

def main():
    products_dict = read_dict('products.csv', 0)
    print(products_dict)
    
    with open('request.csv', 'r') as file:
        csvreader = csv.reader(file)
        next (csvreader) #this skips first line in the csv file

        print()
        print('Requested Items')
        for row in csvreader:
            productnum = row[0]
            productquan = row[1]
            products = products_dict[productnum]
            productname = products[1]
            productprice = products[2]
            print(f'{productname}: {productquan} @ {productprice}')



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