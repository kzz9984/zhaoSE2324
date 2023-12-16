"""
Name: Kevin Zhao
Date: 12/16/23

File: zhao_matingPairs.py

Purpose: Return a set of male-female gerbil pairs from two equal sized sets of males and females
"""

def main():

    # Define sets
    males = {'Dusty', 'Murphy', 'Olaf', 'Dante', 'Gizmo'}
    females = {'Ginger', 'Lily', 'Piper', 'Daisy', 'Elsa'}
    pairs = set()

    # Remove gerbils from males and females to create mating pairs
    for i in range(len(males)):
        pairs.add((males.pop(), females.pop()))
    
    # Print mating pairs
    print(pairs)


main()