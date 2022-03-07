import math

inPut1 = int(input("Enter the # of manufactured items: "))
inPut2 = int(input("Enter the # of items per box: "))

itemNumber = math.ceil(inPut1 / inPut2)
# math.cecil return a whole number and forces the remiander to round up

print()

print(f"For {inPut1} items, packing {inPut2}, you will need {itemNumber} boxes.")
print()