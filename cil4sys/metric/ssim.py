"""
    get_ssim.py

    Structural Similarity Index (SSIM):

    SSIM is a perceptual metric that evaluates the 
    structural similarity between two images.It 
    takes into account luminance,contrast, and
    structure, and values range from -1 to 1, 
    with higher values indicating better similarity

    Args:
        image_1    (numpy array): 
		image_2	   (numpy array):
            
    Returns:
        float : SSIM ratio factor.


©cil4sys
"""
import numpy as np 
from skimage.metrics import structural_similarity as  compare_ssim
 

 
def get_ssim(image_1,image_2):
   
    # check if te input images have the same size 
    height1, width1 = image_1.shape[:2]
    height2, width2= image_2.shape[:2]
   
    if (height1 == height2 and width1 == width2):
        # Images are same size -> calculate SSIM 
        ssim_value = compare_ssim(image_1, image_2,win_size=3)
    else:
        # input aren't the same size -> rezise images 
        target_height=int((height1+height2)/2)
        target_width=int((width1+width2)/2)
        # Resize 
        resized_image_1 = np.resize(image_1,(target_width, target_height))
        resized_image_2 = np.resize(image_2,(target_width, target_height))
        ssim_value= compare_ssim(resized_image_1, resized_image_2, win_size=3)
            
        
        return ssim_value

