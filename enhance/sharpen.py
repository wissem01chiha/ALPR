"""
    sharpen.py 

    amout controller the sharping degree high 
    values more details.
    
    Args:
    -   input_image     (numpy.ndarry)
    -   kernel_size     (tuple)
    -   value 

    Returns:
    -   sharpened       (numpy.ndarry)

©cil4sys  
"""
import cv2

def sharpen(input_image):
    # Apply Gaussian blur to the image
    blurred = cv2.GaussianBlur(input_image, (0, 0), 27)
    sharpened = cv2.addWeighted(input_image, 1 + 5, blurred, -5, 0)

    return sharpened