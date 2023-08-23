"""
    Contrast Limited Adaptive Histogram Equalization
    lipLimit=2.0  tileGridsize=(8.8)

    
"""

  
import cv2

def clahe(IMAGE,CLIP_LIMIT,TITLE_GRID_SIZE):
    
    assert IMAGE is not None, "file could not be read, check with os.path.exists()"
    gray_image = cv2.cvtColor(IMAGE, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=CLIP_LIMIT, tileGridSize=TITLE_GRID_SIZE)
    clahe_img = clahe.apply(gray_image)
   
    return  clahe_img


