""" 
wgne_var.py 

Estimation of white Gaussian noise variance.
 
The module assume that the noise modelis additive white
Gaussian 
assuming that these coefficients mostly represent noise 
rather than image content.
These coefficients are typically located in the top-left corner 
of the DCT matrix
 
Args:
    - image         (numpy.nadarry)
    - block_size    (int)

Returns
    - mean           (float)
    - std_dev        (float)  

©cil4sys
""" 
from scipy.fftpack import dct
import numpy as np
 
def wgne_var(image,block_size=8):
    # Apply the 2D DCT to the input image
    dct_result =dct(dct(image, axis=0, norm='ortho'), axis=1, norm='ortho')
    # Select a block of high-frequency DCT coefficients
    high_freq_block = dct_result[:block_size, -block_size:]
    # Calculate statistics of the high-frequency coefficients
    mean = np.mean(high_freq_block)
    std_dev = np.std(high_freq_block)

    return mean , std_dev 