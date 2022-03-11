from ast import Return
import csv
from socket import create_server

def main():
    products_dict = read_dict('products.csv', 0)
    print(products_dict)
    
    with open('request.csv', 'r') as file:
        csvreader = csv.reader(file)
        next (csvreader) #this skips first line in the csv file

        for row in csvreader:
            productnum = row[0]
            products = products_dict[productnum]
            productname = products[1]
        print()
        print(productname)



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

# products = read_dict('products.csv', 0)
# print(products)
main()