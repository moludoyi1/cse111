
import math


from datetime import datetime

dt =  datetime.now()

print('''Welcome to Mikey's tires. \nPlease enter 0 if you wish to quit/leave''')

choice = input('Do you want use our tire inventory? ')

w = 0
ar = 0
d = 0

while choice != 0:
    if choice.lower() == 'yes':
        print('''    $60/tire
        1. 125/90R16 
        2. 185/60R13
        3. 195/45R15
        4. 165/55R14
        5. Quit''')
        invsize = int(input("What # do you want to use (Please enter between 1 - 5): "))
        if invsize == 1:
            w = 125
            ar = 90
            d = 16
            fs = math.pi * (w ** 2) * ar
            ss = (w * ar) + (2540 * d)
            v = (fs * ss) / 10000000000
            print(f'The volume is {v:.2f} liters')
            print()

            buy = input('Do you wish to buy this tire? ')
            if buy.lower() == 'yes':
                phonenum = int(input('Enter your phone number(numbers only): '))
                print()
                print(f'Total = $60 for 1 tire or $240 for complete set')
                print()
                with open("volume.txt", "at") as volume_file:
                    print(f'{dt:%Y-%m-%d}, {w}, {ar}, {d}, {v:.2f}, {phonenum}', file = volume_file)
                
            else:
                print("Thanks for using our inventory. Please come again!")
            choice = 0

        elif invsize == 2:
            w = 185
            ar = 60
            d = 13
            fs = math.pi * (w ** 2) * ar
            ss = (w * ar) + (2540 * d)
            v = (fs * ss) / 10000000000
            print(f'The volume is {v:.2f} liters')
            buy = input('Do you wish to buy this tire? ')
            if buy.lower() == 'yes':
                phonenum = int(input('Enter your phone number(numbers only): '))
                print(f'Total = $60 for 1 tire or $240 for complete set')
                print()
                with open("volume.txt", "at") as volume_file:
                    print(f'{dt:%Y-%m-%d}, {w}, {ar}, {d}, {v:.2f}, {phonenum}', file = volume_file)
                
            else:
                print("Thanks for using our inventory. Please come again!")
            choice = 0

        elif invsize == 3:
            w = 195
            ar = 45
            d = 15
            fs = math.pi * (w ** 2) * ar
            ss = (w * ar) + (2540 * d)
            v = (fs * ss) / 10000000000
            print(f'The volume is {v:.2f} liters')
            print()

            buy = input('Do you wish to buy this tire? ')
            if buy.lower() == 'yes':
                phonenum = int(input('Enter your phone number(numbers only): '))
                print(f'Total = $60 for 1 tire or $240 for complete set')
                print()
                with open("volume.txt", "at") as volume_file:
                    print(f'{dt:%Y-%m-%d}, {w}, {ar}, {d}, {v:.2f}, {phonenum}', file = volume_file)

            else:
                print("Thanks for using our inventory. Please come again!")
            choice = 0
                
        elif invsize == 4:
            w = 165
            ar = 55
            d = 14
            fs = math.pi * (w ** 2) * ar
            ss = (w * ar) + (2540 * d)
            v = (fs * ss) / 10000000000
            print(f'The volume is {v:.2f} liters')
            print()

            buy = input('Do you wish to buy this tire? ')
            if buy.lower() == 'yes':
                phonenum = int(input('Enter your phone number(numbers only): '))
                print(f'Total = $60 for 1 tire or $240 for complete set')
                print()
                with open("volume.txt", "at") as volume_file:
                    print(f'{dt:%Y-%m-%d}, {w}, {ar}, {d}, {v:.2f}, {phonenum}', file = volume_file)
                
            else:
                print("Thanks for using our inventory. Please come again!")
            choice = 0

        else:
            print("Thanks for using our inventory. Please come again!")
        

    elif choice.lower() == 'no':
        # Get inputs
        w = int(input("Enter the width of the tire in mm (Ex: 225): "))
        ar = int(input("Enter the aspect ratio of the tire (Ex: /70): "))
        d = int(input("Enter the diameter of the tire (Ex: R15): "))
        print()

        # Convert input into formula
        fs = math.pi * (w ** 2) * ar
        ss = (w * ar) + (2540 * d)
        # print()

        # Get output
        v = (fs * ss) / 10000000000
        print(f'The appropriate volume is {v:.2f} liters')
        # print()

        with open("volumes.txt", "at") as volume_file:
            print(f'{dt:%Y-%m-%d}, {w}, {ar}, {d}, {v:.2f}', file = volume_file)
        choice = 0
    else:
        print('Thanks, please proceed')



# # Get inputs
# w = int(input("Enter the width of the tire in mm (Ex: 225): "))
# ar = int(input("Enter the aspect ratio of the tire (Ex: /70): "))
# d = int(input("Enter the diameter of the tire (Ex: R15): "))

# Convert input into formula
# fs = math.pi * (w ** 2) * ar
# ss = (w * ar) + (2540 * d)
# print()

# # Get output
# v = (fs * ss) / 10000000000
# print(f'The appropriate volume is {v:.2f} liters')
# # print()

# with open("volumes.txt", "at") as volume_file:
#     print(f'{dt:%Y-%m-%d}, {w}, {ar}, {d}, {v:.2f}', file = volume_file)