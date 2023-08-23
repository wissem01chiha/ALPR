"""
hsi_transform.py


HSI Image transformation 

The HSI color space separates an image into three
components: hue, saturation, and intensity. 
This transformation is useful for
color manipulation and enhancement in image processing.


©cil4sys
"""
from numba import jit
import numpy as np 

@jit(nopython=True)
def hsi_transform(rgb_image):
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
