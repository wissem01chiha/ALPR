"""
capture_video.py

    function that uses the default raspi camera to get
    video records and store them locally.







©cil4sys
"""

import os
import time 
import cv2
from cv2 import utils
import pkg_resources
import logging
#import warnings


def open_video_source(video_path):
    # Set the logging level to disable all log messages
    
    # Suppress OpenCV warning : 
    #https://docs.opencv.org/4.6.0/da/db0/namespacecv_1_1utils_1_1logging.html
    #cv2.setLogLevel(cv2.CAP_PROP_FRAME_WIDTH, LOG_LEVEL_SILENT=0)
    #cv2.setLogLevel(cv2.CAP_PROP_FRAME_HEIGHT, LOG_LEVEL_SILENT=0)
    
    # Or Suppress OpenCV warnings
    #warnings.filterwarnings("ignore", category=UserWarning, module="cv2")
    
    # Try opening the camera
    cap = cv2.VideoCapture(0)  # 0 represents the default camera (first camera)

    if not cap.isOpened():
        print("[WARN]: Could not open the camera.")
        package_directory = os.path.dirname(pkg_resources.resource_filename(__name__, ''))
        print(f"[INFO]: VideoCapture {os.path.join(package_directory, video_path)}")
        cap = cv2.VideoCapture(os.path.join(package_directory, video_path))

    if not cap.isOpened():
        print("[ERROR]: Could not open the camera or the provided video file.")
        return None
    
    # Reset OpenCV log level to its default state
    #cv2.setLogLevel(cv2.CAP_PROP_FRAME_WIDTH, LOG_LEVEL_DEBUG=5)
    #cv2.setLogLevel(cv2.CAP_PROP_FRAME_HEIGHT, LOG_LEVEL_DEBUG=5)
    
    # Or Reset the warning filter to its default state
    #warnings.resetwarnings()

    return cap
  
  

def capture_video(duration,fps,resolution, frames_path, video_path):

    try:
        cap = open_video_source(video_path) 
        if cap is None:
           return False
          
        # Define the codec and create a VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        # Adjust resolution and FPS as needed
        out = cv2.VideoWriter(frames_path, fourcc, fps, resolution)  
        start_time = time.time()
        frame_count = 0
        while time.time() - start_time < duration:
            ret, frame = cap.read()
            if not ret:
                print("[WARN]: Could not read frame from camera.")
                break
            frame_count += 1
            # Write the frame to the output video
            out.write(frame)
        print(f'Total frames in the video: {frame_count}')
        # Release the resources
        cap.release()
        out.release()
        cv2.destroyAllWindows()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
