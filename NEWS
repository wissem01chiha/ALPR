CHANGES 0.1.3 (2023-12-20)
-----------------
+ Add car tracking module using yolo3 models
  - Tracking car system using yolov3 models
  - Multithreding system
  - multipe OCR options: pytesseract, easyocr, pyocr
  - possible Arabic letter detection
  - Possible multiple pattern of Plate models
  - Video show without saving frame: skipping frames to speed up process
  - Visualize:
    * Blue box of detected car
    * plate number and confidence (White/Black)
    * yellow box if datetime exists in the screen
    
+ Separate frame processing of v0.1.1 and frame processing of v0.1.3 by when add  --video argument
  - if run_cil4sys without --video,  v0.1.1 is executed 
  - if run_cil4sys --video, car tracking and license plate saving is proceeded (v0.1.3)
  
+ run_cil4sys could be run from any directory since cil4sys is installed
  - default video: success detected license plate in 23s with 31/181 saved frames

+ Cleanup capturing Video process in video class
  - write open_video_sources fucntion
  - rewrite video_read, video_split and capture_video
  - resolve conflict between Output_path and video_path


CHANGES 0.1.2 (2023-12-14)
-----------------
+ upgrade opencv-python to 4.6.0.66: ultralytics 8.0.222 requires opencv-python>=4.6.0
+ upgrade scipy to 1.8.1: issue with Ubuntu: undefined symbol: _PyGen_Send




TODO
----
+ Function Decomposition:
  - Break down the main function into smaller functions to improve readability and maintainability. Each function should have a specific responsibility.

+ Logging: 
  - Instead of using print statements for informational messages, consider using Python's logging module. It provides more control over log messages.


+ Limit saving frames if new number plate is detected
  - Use tracking system to detect motion
  - Reduce motion detection to only car
  - Do not save the save car/plate: skip frames

+ Use other ORC that seems to be more efficient
  - Arabic option: try to capture arabic letters
  - Use regex for multiple pattern like: standard tunisian plate, RS, Diplomatic...
  
+ Display video with results
  - Box for ROI
  - Plate number
  - Confidence
  
+ Extract datetime during saving plate number
  - Security video cam displays datetime in the upper-right corner of the screen
  
+ for recorded video:
  - extract video sequence with only car/motion to improve performance