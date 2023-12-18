"""
capture_video.py

    function that uses the default raspi camera to get
    video records and store them locally.







©cil4sys
"""

import time 
import cv2

def capture_video(duration,fps,resolution, output_path):

    try:
        # Open the USB webcam
        cap = cv2.VideoCapture(0)  # 0 represents the default camera (first camera)
        if not cap.isOpened():
            print("Error: Could not open the camera. The default sample video will be proceeded")
            return False
        # Define the codec and create a VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        # Adjust resolution and FPS as needed
        out = cv2.VideoWriter(output_path, fourcc, fps, resolution)  
        start_time = time.time()
        print('Before video reading loop')
        frame_count = 0
        while time.time() - start_time < duration:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame from camera.")
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
