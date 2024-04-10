'''
Name: Kevin Zhao
Date: 04/10/2024
File: imageViewer_Zhao.py

Purpose: Create a simple image viewer app that can scroll through multiple images

'''

from tkinter import *
from PIL import ImageTk, Image

root = Tk()                             # Define root window
root.title("Codemy.com Image Viewer")   # Define window title
root.iconbitmap("codemy.ico")           # Change window icon

# Get images
my_img1 = ImageTk.PhotoImage(Image.open("images/aspen.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/aspen2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/me1.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/me2.png"))
my_img5 = ImageTk.PhotoImage(Image.open("images/me3.png"))

# Define list for images
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

# Define status bar
status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

# Place first image on screen upon initialization
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

# Scrolls to next image
def forward(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()                              # Erase current image
	my_label = Label(image=image_list[image_number-1])  # Replace with new image
	
    # Update button destinations
	button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))
	
    # Disable button on last image
	if image_number == 5:
		button_forward = Button(root, text=">>", state=DISABLED)

    # Place new contents on screen
	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)
	
    # Update status bar
	status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
	status.grid(row=2, column=0, columnspan=3, sticky=W+E)

# Scrolls to previous image
def back(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()                              # Erase current image
	my_label = Label(image=image_list[image_number-1])  # Replace with new image
	
    # Update button destinations
	button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    # Disable button on first image
	if image_number == 1:
		button_back = Button(root, text="<<", state=DISABLED)

    # Place new contents on screen
	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)
	
    # Update status bar
	status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
	status.grid(row=2, column=0, columnspan=3, sticky=W+E)

# Define buttons
button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

# Place buttons and status bar on screen
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)


root.mainloop()