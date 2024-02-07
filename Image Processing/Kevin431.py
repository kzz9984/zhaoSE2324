'''
Kevin431: Read and show an image.
'''
import matplotlib
matplotlib.use('TkAgg') # Must be specified before importing pyplot as plt
import matplotlib.pyplot as plt
import os.path
import numpy as np      # "as" lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 3)
# Show the image data in the first subplot
for i in range(3):
    ax[i].imshow(img)
ax[0].set_xlim(140, 150)    # xlim & ylim values define a zoom-in box
ax[0].set_ylim(450, 440)    # xlim & ylim values define a zoom-in box
ax[1].set_xlim(150, 160)    # xlim & ylim values define a zoom-in box
ax[1].set_ylim(470, 460)    # xlim & ylim values define a zoom-in box
ax[2].set_xlim(115, 125)    # xlim & ylim values define a zoom-in box
ax[2].set_ylim(10, 0)       # xlim & ylim values define a zoom-in box

# Show the figure on the screen
plt.show()