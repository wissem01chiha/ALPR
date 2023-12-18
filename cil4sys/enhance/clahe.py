"""
    clahe.py 

    Contrast Limited Adaptive Histogram Equalization. 

    Args:
    -   image           (numpy.ndarry)

    Returns:
    -   clahe_img       (numpy.ndarry)

©cil4sys  
""" 
import cv2

def clahe(image,clip_limit,title_grid_size):
    assert image is not None, "file could not be read, check with os.path.exists()"
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=title_grid_size)
    clahe_img = clahe.apply(gray_image)
   
    return  clahe_img


