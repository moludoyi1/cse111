"""
Write a Python program named provinces.py that reads the contents
of provinces.txt into a list and then modifies the list.
"""


def main():
    print()
    # Read the contents of a text file named
    # provinces.txt into a list named provinces_list.
    # provinces_txt = open("provinces.txt", "r")
    provinces_list = read_list("provinces.txt")
    
    
    # As a debugging aid, print the entire list.
    # print(provinces_list)
    # print(provinces_txt.read())
    

    # Remove the first element from the list.
    provinces_list.pop(0)
    # print(provinces_list)

    # Remove the first element from the list.
    provinces_list.pop()

    # Replace all occurrrences of "AB" with "Alberta".
    for i in range(len(provinces_list)):
        if provinces_list[i] == 'AB':
            provinces_list[i] = 'Alberta'
    print(provinces_list)
    
    # Call the list.count method which will count the
    # number of times that Alberta appears in the list.
    count = 0
    for i in provinces_list:
        if i == 'Alberta':
            count += 1
    
    print()
    print(f'Alberta ocuurs {count} times in the modified list')
    print()
   

def read_list(filename):
    """Read the contents of a text file into a list
    and return the list that contains the lines of text.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list that will store
    # the lines of text from the text file.
    file_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename) as file_txt:
        # Read the contents of the text
        # file one line at a time.
        for line in file_txt:
            # Remove white space, if there is any,
            # from the beginning and end of the line.
            # Append the clean line of text
            # onto the end of the list.
            file_list.append(line.strip())

    # Return the list that contains the lines of text.
    return file_list

if __name__ == "__main__":
    main()