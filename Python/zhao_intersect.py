"""
Name: Kevin Zhao
Date: 12/16/23

File: zhao_intersect.py

Purpose: Print a dictionary containing the key/value pairs shared by two dictionaries
"""

def main():

    # Define dictionaries
    dict1 = {"red":3, "blue":5, "green":3, "yellow":1, "purple":2, "orange":1}
    dict2 = {"yellow":1, "blue":2, "orange":1, "red":1, "green":3, "purple":4}
    dict3 = {}

    # Loop through dict1 to add the key/value pairs it shares with dict2 to dict3
    for key in dict1:
        if (dict1[key] == dict2.get(key, None)):
            dict3[key] = dict1[key]

    # Print dict3
    for (key, value) in dict3.items():
        print(key, value)


main()