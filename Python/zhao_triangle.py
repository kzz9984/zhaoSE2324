"""
Name: Kevin Zhao
Date: 11/23/23

File: zhao_triangle.py

Purpose: Determine validity and classification of triangle from 3 side lengths
"""

def main():

    # Gather 3 side length inputs
    a = float(input("Enter the first side length: "))
    b = float(input("Enter the second side length: "))
    c = float(input("Enter the third side length: "))

    if not (a + b > c and b + c > a and a + c > b):     # Check if triangle is invalid by Triangle Inequality Theorem
        print("Not a triangle")
    elif a == b and b == c:                             # Check if triangle has all equal side lengths
        print("Equilateral triangle")
    elif a == b or b == c or c == a:                    # Check if triangle has two equal side lengths
        print("Isosceles triangle")
    else:                                               # If all other checks fail, triangle must be scalene
        print("Scalene triangle")

main()  # Call the main() function