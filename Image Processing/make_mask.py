import matplotlib.pyplot as plt
import numpy as np

# PIL is no longer maintained -- it has been replaced with Pillow
# To maintain backwards compatibility, "PIL" name is used for imports
import PIL         

def make_mask(rows, columns, stripe_width):
    '''An example mask generator
    Makes slanted stripes of width stripe_width
    image
    returns an ndarray of an RGBA image rows by columns
    '''
    
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    for row in range(rows):
        for column in range(columns):
            if (row+column)//stripe_width % 2 == 0: 
                # (r+c)//w says how many stripes above/below line y=x
                # Note that this is floored division (eg. 3//2 = 1)
                # The % 2 says whether it is an even or odd stripe
                
                # Even stripe
                image[row][column] = [255, 127, 127, 0] # pale red, alpha=0
            
            else:
                # Odd stripe
                image[row][column] = [255, 0, 255, 255] # magenta, alpha=255
            
    return image
    
if __name__ == "__main__":
    image = make_mask(100,100,20)
    
    fig, ax = plt.subplots(1, 1)
    ax.imshow(image)
    plt.show()            
                       
              
