
"""
   countour_select.py 

    Delete images from a folder based on area and aspect ratio conditions.

    Args:
    - folder_path: Path to the folder containing images.
    - min_area: Minimum allowable area for an image.
    - max_aspect_ratio: Maximum allowable aspect ratio (length/width).

    Returns:
    - bool       : roi_exsit 
    - ditionnary : filtred countours 

©cil4sys
"""
 
def countour_select(countour_list,min_area,min_ratio,max_ratio):
    # filtre countours based on area 
    # suppose the frame has a ROI
    roi_exist=True
    # init filtred countours list of dicts
    filtred_countours=[]
    for i in range(len(countour_list)):
        d=countour_list[i]
        area=d['w']*d['h']
        ratio = d['w'] / d['h']
        if  area > min_area and min_ratio < ratio < max_ratio:
            filtred_countours.append(d)
    if len(filtred_countours) == 0:
        roi_exist=False

    return roi_exist , filtred_countours
