import math
import csv

from datetime import datetime

'Column numbers from csvData.csv file'
STATE_COL = 0
LOWTAX_COL = 1
HIGHTAX_COL = 2

def main():
    print()
    hours = get_hours()

    hourly_rate = get_hourly_pay_rate()

    appx_weekly_pay = (f"${get_weekly_income(hours, hourly_rate)}")
    # print(weekly_pay)
    
    # tax_rate = get_state_income_tax_rate

    state_dict = get_state_income_tax_dict('csvData.csv')
    # print(state_dict)




def get_hours():
    return int(input("How many hours do you typically work per week: "))

def get_hourly_pay_rate():
    return float(input("What's your pay per hour: $"))

def get_weekly_income(h, r):
    return h * r

def get_state_income_tax_rate(state):
    state = input("Which state do you reside in: ")
    return state
    
def get_state_income_tax_dict(filename):
    state_income_tax_dict = {}
    with open(filename) as file:
        csvreader = csv.reader(file)
        next(csvreader)

        for line in csvreader:
            key = line[0]
            state_income_tax_dict[key] = line
    return state_income_tax_dict



def add_missing_income_taxe_rate():
    """Income tax rate in  the csvData file are missing, representing that
    the rate are 0s."""


main()