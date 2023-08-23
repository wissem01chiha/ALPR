"""










"""

import time 
import cv2

def capture_video(DURATION,FPS,RESOLUTION, OUTPUT_PATH):

    try:
        # Open the USB webcam
        cap = cv2.VideoCapture(0)  # 0 represents the default camera (first camera)
        if not cap.isOpened():
            print("Error: Could not open the camera.")
            return False
        # Define the codec and create a VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(OUTPUT_PATH, fourcc, FPS, RESOLUTION)  # Adjust resolution and FPS as needed
        start_time = time.time()
        while time.time() - start_time < DURATION:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame from camera.")
                break
            # Write the frame to the output video
            out.write(frame)
        # Release the resources
        cap.release()
        out.release()
        cv2.destroyAllWindows()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False