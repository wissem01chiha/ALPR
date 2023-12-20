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
import      pkg_resources
from .capture_video import open_video_source

def read_video(video_path):
    try:
      # Open the video source
      cap = open_video_source(video_path)
      if cap is None:
         return 0, 0, 0
        
      # Get the total number of frames in the video
      frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
      exec_time=time.time()
      # Release the resources
      cap.release()
      return 1 , frames  , exec_time
  
    except Exception as e:
      print(f"Error: {e}")
      return 0, 0, 0


def video_split(video_path, frames_output_path, fps):
    try:
        # Open the video source
        vid_cap = open_video_source(video_path)
        if vid_cap is None:
            return 0

        start_time = time.time()
        i = 0
        while vid_cap.isOpened():
            frame_interval = int(vid_cap.get(cv2.CAP_PROP_FPS) / fps)
            success_read_frame, image = vid_cap.read()
            if not success_read_frame:
                break
            if i % frame_interval == 0:
                cv2.imwrite(os.path.join(frames_output_path, f"frame{i}.jpg"), image)
            i += 1

        # Release the resources
        vid_cap.release()

        return time.time() - start_time

    except Exception as e:
        print(f"Error: {e}")
        return 0
