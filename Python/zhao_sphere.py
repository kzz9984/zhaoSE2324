"""
Name: Kevin Zhao
Date: 11/22/23

File: zhao_sphere.py

Purpose: Calculate the diameter, circumference, surface area, and volume of a sphere
"""

import math # Import math module

def main():

    # Gather inputs
    radius = float(input("Please enter the radius of the sphere: "))

    # Calculate values
    diameter = 2 * radius                       # Calculate diameter
    circumference = math.pi * diameter          # Calculate circumference
    surfaceArea = 4 * math.pi * pow(radius, 2)  # Calculate surface area
    volume = (4/3) * math.pi * pow(radius, 3)   # Calculate volume

    # Print values
    print("The diameter is:", round(diameter, 2), "units")                     # Print diameter rounded to 2 decimals
    print("The circumference is:", round(circumference, 2), "units")           # Print circumference rounded to 2 decimals
    print("The surface area is:", round(surfaceArea, 2), "square units")       # Print surface area rounded to 2 decimals
    print("The volume is:", round(volume, 2), "cubic units")                   # Print volume rounded to 2 decimals

main()  # Call the main() function