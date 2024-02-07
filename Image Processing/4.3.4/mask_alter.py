import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw            

def alter_one_image(original_image, percent_of_side=.1):
    """ Splits PIL.Image into 4 sections
    
    original_image must be a PIL.Image
    Returns a new PIL.Image split into 4 sections, where
    0 < percent_of_side < 1 
    is gap width as a portion of the shorter dimension of original_image
    """
    #set the gap width
    width, height = original_image.size
    gap = int(percent_of_side * min(width, height) / 2) # half the gap width in pixels

    ###
    #create a mask
    ###
    
    #start with opaque mask
    mask = PIL.Image.new('RGBA', (width, height), (127,0,127,255))
    drawing_layer = PIL.ImageDraw.Draw(mask)
    
    # Overwrite the RGBA values with A=0.
    
    # Draw two rectangles of transparency
    drawing_layer.polygon([(width/2-gap,0),(width/2+gap,0),
                            (width/2+gap,height),(width/2-gap,height)],
                            fill=(127,0,127,0))
    drawing_layer.polygon([(0,height/2-gap),(0,height/2+gap),
                            (width,height/2+gap),(width,height/2-gap)],
                            fill=(127,0,127,0))
    
    # Make the new image, starting with all transparent
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    result.paste(original_image, (0,0), mask=mask)
    return result
    
def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list

def alter_all_images(directory=None):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and are split into 4 sections.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    # Load all the images
    image_list, file_list = get_images(directory)  

    # Go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        print (n)
        filename, filetype = os.path.splitext(file_list[n])
        
        # Split the image with default percent of gap
        curr_image = image_list[n]
        new_image = alter_one_image(curr_image) 
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    