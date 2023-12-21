import cv2
import numpy as np
import easyocr
from PIL import Image
import threading
import re
import pytesseract
import pyocr
import concurrent.futures
from pyocr.builders import TextBuilder
import os.path
import time
from datetime import datetime as dt
import pkg_resources




# Function to extract datetime from the upper right region
def extract_datetime(frame):
    
    # Crop the region at the upper right (adjust coordinates based on your video)
    #x, y, w, h = 770, 33, 300, 40  # Example coordinates (adjust based on your video)
    x, y, w, h = 300, 33, 300, 40 
    crop_region = frame[y:y + h, x:x + w]

    # Draw a square around the cropped region (BGR)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2) #yellow
    
    # Display the coordinates of the cropped region
    coordinates_text = f"Coordinates: ({x}, {y}), Width: {w}, Height: {h}"
    #cv2.putText(frame, coordinates_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
    #             0.5, (255, 255, 255), 1, cv2.LINE_AA)
    #print(f" This is coordinate of datetime: '{coordinates_text}'")
    
    # Convert the cropped region to RGB (EasyOCR expects RGB format)
    crop_rgb = cv2.cvtColor(crop_region, cv2.COLOR_BGR2RGB)
    
    # Initialize EasyOCR reader for English and Arabic languages
    reader = easyocr.Reader(['en'], gpu=False, verbose=False) #, 'ar'
    
    # Use EasyOCR to extract text from the cropped region
    results = reader.readtext(crop_rgb)
    # Check if there are any results
    if results:
        # Extract confidence score
        #confidence = results[0][2]
        # Check confidence threshold before printing
        #if confidence > 0.95:
                  # If there is only one result, extract datetime directly
        if len(results) == 1:
          # Extract text from the result
            datetime_text = results[0][1]
            datetime_text = datetime_text.replace(' ', '_')
            confidence = results[0][2]
        elif len(results) >= 2:
            # If there are multiple results, concatenate date and time
            date_text = results[0][1]
            confidence = results[0][2]
            time_text = results[1][1]
            #confidence_time= results[1][2]
            datetime_text = f"{date_text}_{time_text}"
            
        print(f"Detected text: '{datetime_text}' with confidence: {confidence}")
        return datetime_text
        #else:
        #    print("Confidence below threshold. Ignoring text.")
        #    return str(datetime_text+" D")
    else:
        print("No text detected.")
        return "NA"
        
    # Extract text from the result (assuming the first result is the most relevant)
    #datetime_text = str(results[0][1])+"__"+str(results[1][1]) if results else ""
    #datetime_text = results[0][1] if results else ""
    

def process_frame(frame, ocr_type, recorded_license_plate, tracker,
                  video_path, recorded_license_plates):
    #print("[INFO] Start frame processing...")
    # Initialize variables
    tracking_started = False
    tracked_object = None
    package_directory = os.path.dirname(pkg_resources.resource_filename(__name__, ''))
    

    # Load Tiny YOLO
    #net = cv2.dnn.readNet("yolo/yolov3-tiny.cfg", "yolo/yolov3-tiny.weights")
    net = cv2.dnn.readNet(os.path.join(package_directory, "yolo/yolov3-tiny.cfg"),
                          os.path.join(package_directory, "yolo/yolov3-tiny.weights"))
    classes = []
    #with open("yolo/coco.names", "r") as f:
    with open(os.path.join(package_directory, "yolo/coco.names"), "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getUnconnectedOutLayersNames()

    # Initialize OCR tool based on the selected type
    if ocr_type == 'tesseract':
        # Path to the Tesseract executable (update this path based on your installation)
        tesseract_path = '/usr/bin/tesseract'
        pytesseract.pytesseract.tesseract_cmd = tesseract_path
    elif ocr_type == 'easyocr':
        reader = easyocr.Reader(['en'], gpu=False, verbose=False)  # Specify languages as needed ,'ar'
    elif ocr_type == 'pyocr':
        # Initialize PyOCR
        tools = pyocr.get_available_tools()
        tool = tools[0]  # Use the first available OCR tool
    else:
        raise ValueError("Invalid OCR type. Choose 'tesseract', 'easyocr', or 'pyocr'.")
 
    height, width, _ = frame.shape

    # Convert BGR to RGB
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outs = net.forward(layer_names)

    # Post-process the outputs
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5 and class_id == 2:  # Class ID 2 corresponds to "car" in COCO dataset
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = center_x - w // 2
                y = center_y - h // 2
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])

    # Non-maximum suppression
    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    for i in indices: #.flatten()
        box = boxes[i]
        x, y, w, h = box
        
        # Ensure all coordinates are non-negative
        #x, y, w, h = max(0, x), max(0, y), max(0, w), max(0, h)
        # Adjust x and w to stay within the frame width
        x = max(0, x)
        w = min(frame.shape[1] - x, w)
    
        # Adjust y and h to stay within the frame height
        y = max(0, y)
        h = min(frame.shape[0] - y, h)
        
        if tracking_started:
              # Update the tracker with the new bounding box
              success, bbox = tracker.update(frame)
              if success:
                 # Start tracking with NEW bounding box (appears of new car for example)
                  x, y, w, h = [int(i) for i in bbox]
                  #print(f" Start tracking with the NEW bounding box with ROI Coordinates: x={x}, y={y}, width={w}, height={h}")
                  # the tracker is re-initialized each time a successful update occurs. 
                  # This might be suitable for scenarios where the tracked object undergoes 
                  #significant changes or occlusion during the tracking, 
                  #and re-initializing helps improve tracking accuracy.
                  tracker.init(frame, (x, y, w, h))
                  tracked_object = (x, y, w, h)
                  cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
  
                  # Crop the region of interest (ROI) for license plate recognition
                  roi = frame[y:y + h, x:x + w]
                  # Process the ROI using your OCR logic (omitted for brevity)
              else:
                  # Tracking failed, reset variables
                  tracking_started = False
                  tracked_object = None
        else:
           # Start tracking with OLD bounding box
            #print(f" Start tracking with OLD bounding box ROI Coordinates: x={x}, y={y}, width={w}, height={h}")
            #initializing the tracker outside of the success condition means that the tracker 
            #is only initialized once when tracking starts. Subsequent updates use the same 
            #tracker without re-initializing it. This approach is suitable when you want to t
            #rack a relatively stable object without frequent re-initializations.
            tracker.init(frame, (x, y, w, h))
            tracking_started = True
            tracked_object = (x, y, w, h)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # Crop the region of interest (ROI) for license plate recognition
            roi = frame[y:y + h, x:x + w]
        # Use the selected OCR tool to extract text from the license plate
        if ocr_type == 'tesseract':
          # Convert the ROI to grayscale for better Tesseract OCR accuracy
            gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray_roi, 150, 255, cv2.THRESH_BINARY_INV)
            custom_config = r'--oem 3 --psm 6 outputbase digits -l ara+eng --tessedit_char_whitelist=0123456789تونس'
             # Tesseract OCR
            txt = pytesseract.image_to_string(thresh, config=custom_config)
            confidence = confidences[i] * 100  # Confidence in percentage
        elif ocr_type == 'easyocr':
            # EasyOCR
            results = reader.readtext(roi)
            txt = results[0][1] if results else ""
            confidence = confidences[i] * 100  # Confidence in percentage
        elif ocr_type == 'pyocr':
            # pyOCR
            txt = tool.image_to_string(
                Image.fromarray(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)),
                lang="ara+eng",
                builder= pyocr.builders.TextBuilder(tesseract_layout=6)
            )
            confidence = confidences[i] * 100  # Confidence in percentage
        else:
            raise ValueError("Invalid OCR type. Choose 'tesseract', 'easyocr', or 'pyocr'.")

        # Find and replace Arabic characters using a more flexible pattern
        # Remove non-alphanumeric characters  تونس
        txt = re.sub(r"[^\d]", "_", txt) 
        # if 'تونس' in txt:
        #     # If 'تونس' is already present, leave the text unchanged
        #     #txt = re.sub(r'[^\w\s]', 'تونس', txt) 
        #     print("tunis is in text")
        #     #pass
        if confidence > 70:
            if is_valid_license_plate(txt):
                print(f"Detected license plate '{txt}' is valid.")
                if is_license_plate_recorded(txt, recorded_license_plates):
                    #print(f"Detected license plate '{txt}' ")
                   break
                else:
                  #print(f"Recorded License Plates: {recorded_license_plates}")
                  print(f"Detected license plate '{txt}' is not recorded. (Confidence: {confidence:.2f}%)")
                  
                  # Extract datetime from the current frame
                  datetime_info = extract_datetime(frame)

                  # Update the dictionary of recorded license plates
                  recorded_license_plates[txt]= datetime_info

                  # Update the list of recorded license plates
                  #recorded_license_plates.append(txt)

                  print(f"DICT: '{recorded_license_plates}'")


                  # Display the datetime information (you may want to further process or use this information)
                  #print(f"Datetime: {datetime_info}")

                  ## Write license to file
                  with open(os.path.splitext(os.path.basename(video_path))[0]+'_licenses.txt',"a") as f: 
                       print(txt.strip("_")+" "+str(round(confidence,2))+" "+datetime_info, file=f) 
            else:
                print(f"Detected license plate '{txt}' is not valid.")
        
        # text to display    
        text_to_display = f"{txt} (Confidence: {confidence:.2f}%)"
       # Draw a filled black rectangle for the text background
        text_size = cv2.getTextSize(text_to_display, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)[0]
        cv2.rectangle(frame, (x, y - 10 - text_size[1]), (x + text_size[0], y - 10), (0, 0, 0), -1)

        # Draw the license plate text on the frame
        cv2.putText(frame, text_to_display, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
    return frame, recorded_license_plate


# List of regex patterns for license plate formats
license_plate_patterns = [
    r'_*\d{1,3}_+\d{1,4}_*',        # Tunisian format  r'\d{1,3}\sتونس\s\d{1,4}'
    r'_*\d{5,6}_+[آ-ي]{2}_*',       # Alternative format RS
    # Add more patterns as needed
]

def is_valid_license_plate(plate):
   # Check if the license plate matches any pattern from the list
    return any(re.fullmatch(pattern, plate) for pattern in license_plate_patterns)
  

def is_license_plate_recorded(plate, recorded_license_plates):
    return plate in recorded_license_plates
        

def process_video(video_path, ocr_type, tracker,recorded_license_plates):
    print(f"Starting Processing Video, {video_path}")
    cap = cv2.VideoCapture(video_path)
    
    
    
        # Create a new file
    with open(os.path.splitext(os.path.basename(video_path))[0] + '_licenses.txt', 'w') as f:
        print("License" " "  "Confidence" " " "Datetime", file=f)
        pass
    
    frame_count = 0
    recorded_license_plate = ""
    with concurrent.futures.ThreadPoolExecutor() as executor:
        while True:
            ret, frame = cap.read()
            if not ret or frame is None:
                break

            frame_count += 1
            
            # Skip frames to speed up processing
            if frame_count % 30 != 0:
                continue

            # Resize the frame to reduce processing time
            frame = cv2.resize(frame, (700, 1000))

            # Submit the frame to the executor for parallel processing
            future = executor.submit(process_frame, frame, ocr_type, 
                              recorded_license_plate, tracker, video_path,
                              recorded_license_plates)

            # Wait for the result and retrieve the processed frame and updated license plate
            processed_frame, recorded_license_plate = future.result()

            cv2.imshow("Frame", processed_frame)

            if cv2.waitKey(30) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

# if __name__ == "__main__":
#   
#     # Start timer
#     start_time = time.time()
#     #video_path = "/media/kirus/BKP250/Camera/Cam16_sorted/20231115/motion/Cam16_20231115_motion_all.avi"
#     video_path = "../video/video1.avi"
#     try:
#       f = open(video_path)
#     except FileNotFoundError:
#       print(f"Video Path: '{video_path}' does not exist!")
#       
#     else:
#          # exists 
#       ocr_type = 'easyocr'  # 'tesseract', 'easyocr', 'pyocr'
#       recorded_license_plates={}
#       
#       # Initialize object tracker (using MIL/KCF tracker)
#       tracker = cv2.TrackerMIL_create()
#       #tracker = cv2.TrackerKCF_create()
#       #tracker = cv2.TrackerCSRT_create()
#       #tracker = cv2.legacy.TrackerMOSSE_create()
#       
#       process_video(video_path, ocr_type, tracker)
#       # End timer
#       end_time = time.time()
#       # Calculate elapsed time
#       elapsed_time = end_time - start_time
#       print("Elapsed time: ", dt.strftime(dt.utcfromtimestamp(elapsed_time), '%Hh:%Mm:%Ss'))
