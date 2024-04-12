'''
Name: Kevin Zhao
Date: 04/12/2024
File: matPlot_Zhao.py

Purpose: Create a GUI-based MatPlotLib Python program to display house price data

'''

from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()                                                 # Define root window
root.title('Codemy.com - Learn To Code!')                   # Set window title
root.iconbitmap("codemy.ico")                               # Set window icon
root.geometry("400x200")                                    # Set window size

def graph():                                                # Create function to generate graph
	house_prices = np.random.normal(200000, 25000, 5000)    # Generate random data with normal distribution
	plt.hist(house_prices, 50)                              # Create histogram with 50 bins
	plt.show()                                              # Show graph

my_button = Button(root, text="Graph It!", command=graph)   # Create button to call graph function
my_button.pack()                                            # Place button on screen

root.mainloop()