"""
wb_ratio.py 

Function that calculate the white and balck
color propostion in colored image (Tunisien licence 
plate are often black and white )

Args:
    image

Return:
    w_ratio  (float)
    b_ratio  (float)

©cil4sys    
"""
import cv2
import numpy as np

def wb_ratio(image):
    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Calculate the proportion of white and black pixels
    total_pixels = grayscale_image.size
    white_pixels = np.sum(grayscale_image == 255)
    black_pixels = np.sum(grayscale_image == 0)
    
    w_ratio = white_pixels / total_pixels
    b_ratio = black_pixels / total_pixels
    
    return w_ratio, b_ratio