import csv

from datetime import datetime

'Column numbers from csvData.csv file'
STATE_COL = 0
LOWTAX_COL = 1
HIGHTAX_COL = 2

def main():
    try:
        print()
        hours = get_hours()

        hourly_rate = get_hourly_pay_rate()

        appx_weekly_pay = get_weekly_income(hours, hourly_rate)
        print(appx_weekly_pay)

        state_residence = get_dict_key()
        
        state_dict = get_state_income_tax_dict('csvData.csv')
        # print(state_dict)

        tax_rate = get_state_income_tax_rate(state_dict, state_residence)
        print(f"State Income Tax Rate: {tax_rate:.4f}%")

        pay_after_tax = calculate_weekly_pay(appx_weekly_pay, tax_rate)
        print(f'Pay after tax: ${pay_after_tax:.2f}')

        weekly_bills_save = get_bills()
        weekly_total = sum(weekly_bills_save[1])
        print(f"You need to save a total of ${weekly_total:.2f} each week for your bills")
        
    except KeyError as val_err:
        print("Error:", val_err)
        print("State is incorrecly spelt")

def get_hours():
    return int(input("How many hours do you typically work per week: "))

def get_hourly_pay_rate():
    return float(input("What's your pay per hour: $"))

def calculate_weekly_pay(weekly_pay, tax_rate):
    tax = weekly_pay * tax_rate
    weekly_pay = weekly_pay - tax
    return weekly_pay

def get_weekly_income(h, r):
    return h * r

def get_dict_key():
    state = input("Which state do you reside in: ")
    return state

def get_state_income_tax_rate(state_income_tax_dict, state):
    # print(float(state_income_tax_dict[state] [LOWTAX_COL]))
    state = float(state_income_tax_dict[state] [LOWTAX_COL])
    # state = r * 100
    # print(f"State Income Tax Rate: {state:.2f}")
    return state
    
def get_state_income_tax_dict(filename):
    state_income_tax_dict = {}
    with open(filename) as file:
        csvreader = csv.reader(file)
        next(csvreader)

        for line in csvreader:
            key = line[STATE_COL]
            state_income_tax_dict[key] = line
    return state_income_tax_dict

def get_bills():
    bills = []
    payments = []
    continueon = True
    while continueon == True:
        print()
        print('''Please select on of the options:
        1. Add bills
        2. Done adding bills''')
        option = int(input("Please enter an option: "))
        
        if option == 1:
            print()
            bill = input("What bill would you like to add: ")
            bills.append(bill)
            payment = float(input(f"What is the monthly cost of {bill}? $"))
            payment = payment/4
            payments.append(payment)
        else:
            continueon = False
        

    bills_and_payments = [bills,payments]
    return bills_and_payments

if __name__ == "__main__":
    main()