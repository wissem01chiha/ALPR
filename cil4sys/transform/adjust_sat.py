"""
adjust_sat.py 

saturation image adjustement using HSI
color base transformation.

©Cil4Sys
"""
from .hsi  import *

def adjust_sat(rgb_image, factor):
    hsi_image=hsi_to_rgb(rgb_image)
    hsi_image[:, :, 1] *= factor
    rgb_adjusted=hsi_to_rgb(hsi_image)
    
    return rgb_adjusted






