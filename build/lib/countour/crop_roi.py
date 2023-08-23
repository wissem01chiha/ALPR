"""
    crop_roi.py 

    Function that crops a region of an image based on an 
    image countour. 

    Args:
    -  List         : countour_list 
    -  numpy.ndarry : image 

    Returns:
    -list           : result_list 

©cil4sys  
"""

from functools 	import 	partial
 
def extract_rect_region(COUNTOUR_DICT,IMAGE):
    x, y, h ,w =COUNTOUR_DICT['x'], COUNTOUR_DICT['y'],COUNTOUR_DICT['h'], COUNTOUR_DICT['w']
    rect_region = IMAGE[y:y+h, x:x+w]
    return rect_region 

def crop_roi(COUNTOUR_LIST,IMAGE):
    partial_function = partial(extract_rect_region,IMAGE=IMAGE)
    result=map(partial_function,COUNTOUR_LIST)
    result_list=list(result)

    return  result_list