import cv2
"""
    takes a numpy nadrry image format and detect rectangular shapes into
    return the rectangular into  a dictionnary 

"""


def rectangle_detection(IMAGE):
    
    image = cv2.cvtColor(IMAGE, cv2.COLOR_BGR2GRAY)
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
     