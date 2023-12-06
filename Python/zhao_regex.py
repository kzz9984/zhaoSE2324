"""
Name: Kevin Zhao
Date: 12/04/23

File: zhao_regex.py

Purpose: Write a program to look for lines of the form: “New Revision: 39772”
         and extract the number from each of the lines. Compute and print out the
         average of the numbers.
"""

import re                           # Import Python regex library

def main(): 

    f = open('L10_mbox-short.txt', 'r')
    total = 0                       # Sum of extracted numbers
    n = 0                           # Count of extracted numbers

    for line in f:
        line = line.rstrip()        # Remove all trailing whitespace
        num = re.findall('^New Revision: (\d+)$', line)
        if len(num) > 0:            # Check whether number was extracted
            total += int(num[0])    # Add extracted number to sum
            n += 1                  # Increment count by 1
    
    print('Average:', round(total/n, 3))

main()