'''Team Activity'''

from datetime import datetime

subtotal = float(input("Enter your subtotal: "))

today = datetime.now()
day = today.weekday()

# Note: Monday = 0 while Sunday = 6

total = 0
new_subtotal = 0
y = 0
x = 0
salestax = 0

while subtotal != 0:
    if subtotal >= 50:
        if day == 1 or day == 2:
            discount = 0.1 * subtotal
            new_subtotal = subtotal - discount
            salestax = 0.06 * new_subtotal
            total = salestax + new_subtotal
        print(f"Discount amount: {discount:.2f}")
        print(f'Sales Tax amount: {salestax:.2f}')
        print(f'TOtal amount due: {total:.2f}')
    else:
        salestax = 0.06 * subtotal
        total = subtotal + salestax
    print(f'Sales Tax amunt: {salestax:.2f}')
    print(f'Total Amount due: {total:.2f}')
