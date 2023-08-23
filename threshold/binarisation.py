"""
    binarisation.py

    function that threshold the image based on a specific rgb
    range color.

    Args:
        image  (numpy array): input colored image.
		
    Returns:
        Numpy Array : frame.

    Notes:
        The actual version use the Green  as a thresh color.

    ©cil4sys
    """
import cv2
import numpy as np 

def binarisation(image):
    # binarisation of the image 
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_color = np.array([40, 40, 40])   
    upper_color= np.array([80, 255, 255])
    mask = cv2.inRange(hsv_image, lower_color, upper_color)
    result = np.zeros_like(image)
    # Set green pixels to white in the result image
    result[mask > 0] = [255, 255, 255]
   
    return  result