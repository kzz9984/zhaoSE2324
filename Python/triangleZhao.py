# Name: Kevin Zhao
# Date: 11/22/23

# File: triangleZhao.py

# This program calculates the area of a right triangle

def main():

    # Gather inputs
    base = float(input("Please enter the base of the triangle: "))
    height = float(input("Please enter the height of the triangle: "))

    area = base * height                    # Calculate area

    print("The area is:", round(area, 3))   # Print result rounded to 3 decimals

main()  # Call the main() function