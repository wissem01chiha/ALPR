import 		cv2
from 		PIL 	  import 	Image
from 		skimage.filters import threshold_otsu

"""
    motion_detection.py

    A more detailed explanation of what the function does and why it's used.

    Args:
        background 		(numpy array): Description of the parameter.
		frame	   		(numpy array):
		min_cnt_area 	(float)		:
		max_cnt_area	(float) 	:
            
    Returns:
        (Numpy Array) : frame.
            
    Raises:
        ExceptionType: Description of when and why this exception might be raised.
            Additional details about the possible exceptions if necessary.

    Notes:
        Any additional notes or considerations about the function.
""" 

def motion_detection(background,frame,min_cnt_area,max_cnt_area):
	if frame is not None:
		diff = cv2.absdiff(background, frame)
		gary_diff=cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
		thresh_value = threshold_otsu(gary_diff)
		# Apply binary thresholding using the Otsu's threshold value
		_, binary_image = cv2.threshold(gary_diff,thresh_value, 255, cv2.THRESH_BINARY)
		# find images countours 
		cnts,_ = cv2.findContours(binary_image,
	            	cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		
		for contour in cnts:
			contour_area=cv2.contourArea(contour)
			if contour_area < max_cnt_area and contour_area > min_cnt_area :
				(x,y,w,h) = cv2.boundingRect(contour)
				cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0), 2)
	return frame
