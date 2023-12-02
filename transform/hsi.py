"""
rgb_to_hsi.py

HSI Image transformation 

The HSI color space separates an image into three
components: hue, saturation, and intensity. 
This transformation is useful for
color manipulation and enhancement in image processing.

Args:
    - rgb_image 
Returns:
    - hsi_image 

©Cil4Sys
"""
import numpy as np 

def rgb_to_hsi(rgb_image):
    # Normalize the RGB values to the range [0, 1]
    r, g, b = rgb_image[:, :, 0] / 255.0, rgb_image[:, :, 1] / 255.0, rgb_image[:, :, 2] / 255.0
    # Calculate the Intensity (I)
    intensity = (r + g + b) / 3.0
    # Calculate the Hue (H)
    num = 0.5 * ((r - g) + (r - b))
    den = np.sqrt((r - g)**2 + (r - b) * (g - b))
    theta = np.arccos(num / (den + 1e-5))
    hue = np.where(b <= g, theta, 2.0 * np.pi - theta)
    # Calculate the Saturation (S)
    saturation = 1.0 - (3.0 / (r + g + b + 1e-5)) * np.minimum.reduce([r, g, b])
    # Stack the HSI channels and return the HSI image
    hsi_image = np.stack((hue, saturation, intensity), axis=-1)
    return hsi_image

"""
hsi_to_rgb.py 

HSI inverse transofrmation function 

Args:
    - hsi_img (numpy.ndarry)
Retruns:
    - rgb_img (numpy.ndarry)

©cil4sys
"""

def hsi_to_rgb(hsi_img):
    h, s, i = hsi_img[:, :, 0], hsi_img[:, :, 1], hsi_img[:, :, 2]
    
    x = s * np.cos(h)
    y = s * np.sin(h)
    
    r = i + 2 * x - y
    g = i + x + y
    b = i - (x + y)
    
    rgb_img = np.stack((r, g, b), axis=-1)
    # Clip values to the range [0, 1]
    rgb_img = np.clip(rgb_img, 0, 1) 
    return rgb_img