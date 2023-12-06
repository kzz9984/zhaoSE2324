"""
Name: Kevin Zhao
Date: 11/25/23

File: zhao_stats.py

Purpose: Calculate the mean and standard deviation of a list of numbers
"""

import math         # Import math module

def getInputs():
    """Returns a list of values entered by the user"""

    '''Teacher Solution'''
    # Split string of numbers on space character
    numbers_string = input("Enter list of numbers separated by spaces: ").split()

    # List comprehension to generate list of floats
    numbers = [float(number) for number in numbers_string]

    '''Your Code'''
    numbers = []    # List to store the set of numbers

    # Gather inputs
    n = int(input("How many numbers are in the set? "))

    for i in range(n):
        number = float(input("Enter number " + str(i+1) + ": "))
        numbers.append(number)  # Append each value to the list
    
    return numbers  # Return the list to the main function 


def xBar(list):
    """Returns the mean of the values in list"""

    sum = 0

    for number in list:     # Iterate through the list of values
        sum += number       # Sum the values in the list
    
    return sum/len(list)    # Return the mean to the main function


def stdDev(list):
    """Returns the sample standard deviation of the values in list"""

    sum = 0

    for number in list:                     # Iterate through the list of values
        sum += pow(number - xBar(list), 2)  # Sum the squares of each value's distance to the mean
    
    return math.sqrt(sum/(len(list) - 1))   # Return the standard deviation to the main function


def main():

    numbers = getInputs()   # Gather inputs

    # Print mean rounded to 3 decimals
    print("Mean:", round(xBar(numbers), 3))

    # Print sample standard deviation rounded to 3 decimals
    print("The sample standard deviation is:", round(stdDev(numbers), 3))


main()
