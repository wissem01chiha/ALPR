"""
    crop_roi.py 

    Function that crops a region of an image based on an 
    image countour. 

    Args:
    -   countour_list   (List) 
    -   image           (numpy.ndarry)

    Returns:
    -   result_list     (list)

©cil4sys  
"""
from functools 	import 	partial
 
def extract_rect_region(countou_dict,image):
    x, y, h ,w =countou_dict['x'], countou_dict['y'],countou_dict['h'], countou_dict['w']
    rect_region = image[y:y+h, x:x+w]
    return rect_region 

def crop_roi(countour_list,image):
    partial_function = partial(extract_rect_region,image=image)
    result=map(partial_function,countour_list)
    result_list=list(result)

    return  result_list