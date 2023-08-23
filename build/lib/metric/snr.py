"""
get_snr.py

Signal-To-Noise-Ratio(SNR) 

SNR is a  metric that evaluates the desired signal 
strength to the background noise level.The larger 
the SNR value, the clearer and more distinguishable
the signal is from the noise.

Notes:
    We assume that the noise Model is White gaussin additive noise.

    
©cil4sys
"""

import numpy as np

from numba import jit

@jit(nopython=True)
def get_snr(image):
    mean= np.mean(image)
    std_dev=np.std(image)
    snr_ratio=mean/std_dev
    
    return  snr_ratio