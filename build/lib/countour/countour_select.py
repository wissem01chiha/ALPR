
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
 

def countour_select(COUNTOUR_LIST,MIN_AREA,MIN_RATIO,MAX_RATIO):
    # filtre countours based on area 
    # suppose the frame has a ROI
    roi_exist=True
    # init filtred countours list of dicts
    filtred_countours=[]
    for i in range(len(COUNTOUR_LIST)):
        d=COUNTOUR_LIST[i]
        area=d['w']*d['h']
        ratio = d['w'] / d['h']
        if  area > MIN_AREA and MIN_RATIO < ratio < MAX_RATIO:
            filtred_countours.append(d)
    if len(filtred_countours) == 0:
        roi_exist=False

    return roi_exist , filtred_countours
