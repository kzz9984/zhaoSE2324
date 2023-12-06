# Name: Kevin Zhao
# Date: 11/22/23

# File: averageZhao.py

# This program averages test scores

def main():

    # Gather number of test scores
    num = int(input("Please enter the number of test scores to be averaged: "))

    # Gather test scores and calculate sum
    total = 0
    for i in range(num):
        score = int(input("Please enter test score #" + str(i + 1) + ": "))
        total += score
    
    # Calculate average of test scores
    average = total / num

    # Print average rounded to the nearest integer
    print("The average is:", round(average))

main()  # Call the main() function