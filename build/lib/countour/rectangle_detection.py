"""
    rectangle_detection.py 

    takes a numpy nadrry image format and detect 
    rectangular shapes into.
    
    Args:
    -   countour_list   (List) 
    -   image           (numpy.ndarry)

    Returns:
    -   rectangles     (dict)

©cil4sys  
"""
import cv2

def rectangle_detection(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # init list of dicts for image rectangles
    rectangles=[]
    cnts, _ = cv2.findContours(image, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        # init the dict 
        d={}
        (x,y,w,h)=cv2.boundingRect(contour)
        d["x"]=x
        d["y"]=y
        d["w"]=w
        d["h"]=h
        rectangles.append(d)
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,125), 2)
        del d
    del cnts 

    return rectangles
     