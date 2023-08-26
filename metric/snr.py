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
from .wgne_var import *
 
def get_snr(image,block_size):
    mean= np.mean(image)
    _,std_dev=wgne_var(image,block_size)
    snr_ratio=np.float64(mean/std_dev)
    
    return  snr_ratio