"""
video_split.py 

    function that given a video record, spilt into frames and 
    save them in  a local floder.

Args:
        String : video folder path .
Returns:
        float :  execution time 

"""
import      time 
import      os 
import      cv2
import      multiprocess


def read_video(VIDEO_PATH):
     
    success=1
    # Open the video file  
    cap = cv2.VideoCapture(VIDEO_PATH)
    # Check if the video file was opened successfully
    if not cap.isOpened():
        success=0
    else:
    # Get the total number of frames in the video
        frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    exec_time=time.time() 

    return success , frames  , exec_time


def video_split(VIDEO_PATH,FRAMES_OUTPUT_PATH,FPS):
    start_time = time.time()
    vidCap = cv2.VideoCapture(VIDEO_PATH)
    i=0
    while vidCap.isOpened():
            frame_interval = int(vidCap.get(cv2.CAP_PROP_FPS) / FPS)
            success_read_frame , image = vidCap.read()
            if(success_read_frame==False): 
                break
            if i % frame_interval == 0:
                 cv2.imwrite(os.path.join(FRAMES_OUTPUT_PATH,"frame%d.jpg" % i), image)
            i+=1
    return time.time() - start_time