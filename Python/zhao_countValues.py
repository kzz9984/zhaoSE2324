"""
Name: Kevin Zhao
Date: 12/16/23

File: zhao_countValues.py

Purpose: Print a user-entered dictionary and return the number of unique values it contains
"""

def main():

    # Define dictionary
    dict = {}

    # Gather key-value pairs from user input
    entries = int(input('How many dictionary entries? '))
    for entry in range(entries):
        key = input('Please enter a key: ')
        value = int(input('Please enter a value: '))
        dict[key] = value

    # Count unique values
    unique = []
    for (key, value) in dict.items():
        if (value not in unique):
            unique.append(value)
    print(f'There are {len(unique)} unique values in the dictionary')

    # Print dictionary
    for (key, value) in dict.items():
        print(key, value)


main()