####################################################################
#                                                                  #
#   CAR LICENCING PLATE DETECTION AND RECOGNITION EMBEDDED         #
#   APPLICATION FOR PARCKING INTELLIGENT SYSTEMS.                  #
#                                                                  #
# Developped by :                                                  #
#                                                                  #
#           Cil4Sys - Engineering Tunisia Augest 2023              #
#                                                                  #
# Author :                                                         #
#                                                                  #
#           WISSEM CHIHA   -  Intern                               #
#           Multidisciplinary Engineering Student                  #
#           Polytechnic School of Tunisia                          #
#           Carthage University, Tunis, Tunisia                    #
#                                                                  #
# License:                                                         #
#                                                                  #
#           GNU GENERAL PUBLIC LICENSE                             #
#                                                                  #
# Discussion :                                                     #
#                                                                  #
#           The script Takes a video capture from the default      #
#           raspi camera and store it in the data/videos dir       #
#           then it splits it's frames and output in the data      #
#           /frames dir                                            #
#           PART1 : image processing of each frames in order       #
#           in order to get the possibles lps --> put them in a    #
#           subfolder                                              #
#           PART2 : ocr application to extract lp numbers /chars   #
#                                                                  #
####################################################################
#===================================================================
#           IMPORTING NECESSERAY PYTHON LIBS AND MODULES 
#===================================================================
import      time 
import      os 
import      json
import      cv2
import      time 
import      subprocess
import      numpy as np 
import      pytesseract
from        skimage import  filters
from        PIL  import Image
 

import      transform 
import      utils
import      enhance
import      threshold 
import      video 
import      countour 
import      metric 
 
#===================================================================
#           STARTING BASIC CONFIGURATION PROCESSUS  
#===================================================================
start_time=time.time()
print("[INFO] Configuring Environment ...")
#utils.lcd_display("Configuring Environment")

#subprocess.run("config/raspi.sh", shell=True)

if not os.path.exists("data/images/roi_frames"):
    os.makedirs("data/images/roi_frames")
if not os.path.exists("data/images/video_frames"):
    os.makedirs("data/images/video_frames")
if not os.path.exists("data/videos"):
    os.makedirs("data/videos")
#-------------------------------------------------------------------
#               Read Global Script Vars  
#-------------------------------------------------------------------
print("[INFO] Reading Variable Files ...")

with open('config/var.json') as json_file:
    var = json.load(json_file)
with open('config/path.json') as json_file:
    path=json.load(json_file)

##paths##
VIDEO_PATH                  = path["video_path"]
VIDEO_FRAMES_PATH           = path["frames_path"]
ROI_FRAMES_PATH             = path["roi_path"]

## vars ###
COUNTOUR_AREA               = var["COUNTOUR_AREA"]
MIN_AREA                    = var["MIN_AREA"]
MIN_WIDTH, MIN_HEIGHT       = var["MIN_WIDTH"], var["MIN_HEIGHT"]
MIN_RATIO, MAX_RATIO        = var["MIN_RATIO"], var["MAX_RATIO"]
SSIM_THRESH_RATIO           = var["SSIM_THRESH_RATIO"]

MAX_DIAG_MULTIPLYER         = var["MAX_DIAG_MULTIPLYER"]
MAX_ANGLE_DIFF              = var["MAX_ANGLE_DIFF"]
MAX_AREA_DIFF               = var["MAX_AREA_DIFF"]
MAX_WIDTH_DIFF              = var["MAX_WIDTH_DIFF"]
MAX_HEIGHT_DIFF             = var["MAX_HEIGHT_DIFF"]
MIN_N_MATCHED               = var["MIN_N_MATCHED"]
PLATE_WIDTH_PADDING         = var["PLATE_WIDTH_PADDING"]
PLATE_HEIGHT_PADDING        = var["PLATE_HEIGHT_PADDING"]
MIN_PLATE_RATIO             = var["MIN_PLATE_RATIO"]
MAX_PLATE_RATIO             = var["MAX_PLATE_RATIO"]



#===================================================================
#               RECORD VIDEO  AND EXTRACT FRAMES
#===================================================================
print("[INFO] Starting Video Processing")
print("[INFO] Capturing video ...")
CAPTURE_SUCESS=video.capture_video(10,5,(480,640),video_path)
t=time.time()-start_time
print("[SUCESS] video captured in %d seconds" % t )
read_success, frames_nb , read_time=video.read_video(VIDEO_PATH)
print("[INFO] Generating Frames ...")
if(read_success):
    split_time=video.video_split(VIDEO_PATH,VIDEO_FRAMES_PATH,10)

t=time.time()-start_time
print("[SUCESS] %d frames generated in %d seconds"%(frames_nb,t))
print("[INFO] Preprocessing Frames ...")
#===================================================================
#               PREPROCESSING VIDEO FRAMES  
#===================================================================
# Get a list of frame filenames
frame_files = sorted(os.listdir(VIDEO_FRAMES_PATH))
# Initialize a variable to hold the background  frame
background_frame = None
for frame_index, frame_id in enumerate(os.listdir(VIDEO_FRAMES_PATH)) :
    #get the current frame 
    frame=cv2.imread(os.path.join(VIDEO_FRAMES_PATH, frame_id))
    if background_frame is not None:
        # detect motion in video frames 
        motion_frame=video.motion_detection(background_frame,frame,1000,60000 )
        # binarisation 
        binary_image=threshold.binarisation(motion_frame)
        image_rects=countour.rectangle_detection(binary_image)
        selection_sucess, candidate_rects=countour.countour_select(image_rects,3000,1.2,2.3)
        if(selection_sucess):
            # get the list of the roi's for the frame  
            roi_image=countour.crop_roi(candidate_rects,frame)
            # applying histogram equalisation on ROI detected
            enhanced_roi_dict={}
            for j in range(len(roi_image)):
                adjusted_image=enhance.clahe(roi_image[j],3.5,(30,30)) # <numpy.ndarray>
                # i : frame number treated 
                # j : roi region detected 
                enhanced_roi_dict[(frame_index,j)]=adjusted_image
                pil=Image.fromarray(roi_image[j])
                pil.save(os.path.join(ROI_FRAMES_PATH,"out%dframe%d.jpg" % (j,frame_index)))
            del roi_image
    # update the background frame 
    background_frame=frame 

t=time.time()-start_time
print("[SUCESS] frames preprocessed in %d seconds"%t)   
print("[INFO] Filtring and Denoisng Frames ...")
#===================================================================
#               FRAME FILTRING AND DENOISING   
#===================================================================
# loop for ROI frames and delete similiar images based on SNR ratio 
# Get a list of frame filenames
roi_frame_files = sorted(os.listdir(ROI_FRAMES_PATH)) 
# Initialize a variable to hold the first ROI frame
roi_background_frame = None
for roi_frame_index, roi_frame_id in enumerate(os.listdir(ROI_FRAMES_PATH)):
    #get the current frame 
    frame=cv2.imread(os.path.join(ROI_FRAMES_PATH,roi_frame_id)).copy()
    if roi_background_frame is not None :
        ssim_ratio=metric.get_ssim(roi_background_frame,frame)
        if ssim_ratio is not None:
            if abs(ssim_ratio) > np.float64(SSIM_THRESH_RATIO ) :
                # Perfect image similarity
                os.remove(os.path.join(ROI_FRAMES_PATH,roi_frame_id))
    # update the background frame 
    roi_background_frame=frame 
    
t=time.time()-start_time
print("[SUCESS] frames filtred and denoised in %d seconds"%t)
#=========================================================================
#                       ROI IMAGES SORTING AND ADJUSTEMENT 
#=========================================================================
# Initialize a dict to store frames score  values
score_dict  =   {}
for roi_frame_index, roi_frame_id in enumerate(os.listdir(ROI_FRAMES_PATH)):
    #get the current frame 
    frame=cv2.imread(os.path.join(ROI_FRAMES_PATH,roi_frame_id))
    # Estimation of noise and black color parmeters in each image : --> calculte weighted score 
    frame_score= 1.5 *metric.black_ratio(frame) + 0.4 * metric.get_snr(frame,8)
    score_dict[ roi_frame_id]=frame_score

# Sort the dictionary based on scores values
sorted_dict = dict(sorted(score_dict.items(), key=lambda item: item[1]))
t=time.time()-start_time
print("[INFO] frames sorted in %d seconds"%t)
print("[INFO] Numerical Character Detection ... ")
#===================================================================
#                   SELECT COUNTOURS BY CHAR SIZE     
#===================================================================
#-------------------------------------------------------------------
#                       Image Segmenation 
#-------------------------------------------------------------------
for  roi_frame_id in sorted_dict.keys() :
    #get the current frame 
    frame=cv2.imread(os.path.join(ROI_FRAMES_PATH,roi_frame_id)) 
    # Convert to gray scale 
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # Image Thresholding
    thresh = filters.threshold_otsu(gray_frame)
    binary_frame= gray_frame > thresh
    #-------------------------------------------------------------------
    # Find Image Countours and Select Them By Char Size 
    #-------------------------------------------------------------------
    contours_dict = []
    height, width = binary_frame.shape[:2]
    binary_frame = np.asarray(binary_frame, dtype="uint8")
    contours, _ = cv2.findContours(binary_frame, mode=cv2.RETR_LIST,method=cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        #selcting countours we've calculating the rectangular bounding box 
        # based on area -> eliminate small ones 
        if(cv2.contourArea(contour)> 10):
            x, y, w, h = cv2.boundingRect(contour)
            # insert to dict
            contours_dict.append({
                'x': x,
                'y': y,
                'w': w,
                'h': h,
                'cx': x + (w / 2),
                'cy': y + (h / 2)  
                })
            
    # Select for each frame candidate recatngular countours by area and aspect ratio 
    # and store them in a list of dicts 
    candidate_cnts = []
    k = 0
    for d in contours_dict:
        area = d['w'] * d['h']
        ratio = d['w'] / d['h']
    
        if area > MIN_AREA \
        and d['w'] > MIN_WIDTH and d['h'] > MIN_HEIGHT \
        and MIN_RATIO < ratio < MAX_RATIO:
            d['idx'] = k
            k += 1
            candidate_cnts.append(d)
    #-------------------------------------------------------------------
    #  Select Candidates by Arrangement of Contours
    #-------------------------------------------------------------------
    result_idx = countour.find_chars(candidate_cnts,
                                    MAX_DIAG_MULTIPLYER = 2,  
                                    MAX_ANGLE_DIFF = 10.0, 
                                    MAX_AREA_DIFF = 0.7, 
                                    MAX_WIDTH_DIFF = 0.3,
                                    MAX_HEIGHT_DIFF = 0.3,
                                    MIN_N_MATCHED= 3)

    matched_result = []
    for idx_list in result_idx:
        matched_result.append(np.take(candidate_cnts, idx_list))
    #-------------------------------------------------------------------
    #               Rotate Plate Images 
    #-------------------------------------------------------------------
    plate_imgs = []
    plate_infos = []

    for i, matched_chars in enumerate(matched_result):
        sorted_chars = sorted(matched_chars, key=lambda x: x['cx'])

        plate_cx = (sorted_chars[0]['cx'] + sorted_chars[-1]['cx']) / 2
        plate_cy = (sorted_chars[0]['cy'] + sorted_chars[-1]['cy']) / 2
    
        plate_width = (sorted_chars[-1]['x'] + sorted_chars[-1]['w'] - sorted_chars[0]['x']) * PLATE_WIDTH_PADDING
    
        sum_height = 0
        for d in sorted_chars:
            sum_height += d['h']

        plate_height = int(sum_height / len(sorted_chars) * PLATE_HEIGHT_PADDING)
    
        triangle_height = sorted_chars[-1]['cy'] - sorted_chars[0]['cy']
        triangle_hypotenus = np.linalg.norm(
            np.array([sorted_chars[0]['cx'], sorted_chars[0]['cy']]) - 
            np.array([sorted_chars[-1]['cx'], sorted_chars[-1]['cy']])
        )
    
        angle = np.degrees(np.arcsin(triangle_height / triangle_hypotenus))
    
        rotation_matrix = cv2.getRotationMatrix2D(center=(plate_cx, plate_cy), angle=angle, scale=1.0)
    
        img_rotated = cv2.warpAffine(binary_frame, M=rotation_matrix, dsize=(width, height))
    
        img_cropped = cv2.getRectSubPix(
            img_rotated, 
            patchSize=(int(plate_width), int(plate_height)), 
            center=(int(plate_cx), int(plate_cy))
        )
    
        if img_cropped.shape[1] / img_cropped.shape[0] < MIN_PLATE_RATIO or img_cropped.shape[1] / img_cropped.shape[0] < MIN_PLATE_RATIO > MAX_PLATE_RATIO:
            continue
    
        plate_imgs.append(img_cropped)
        plate_infos.append({
        'x': int(plate_cx - plate_width / 2),
        'y': int(plate_cy - plate_height / 2),
        'w': int(plate_width),
        'h': int(plate_height)
        })
    #-------------------------------------------------------------------
    #                 Get Chars And Digits of The Plate 
    #-------------------------------------------------------------------
    plate_chars = []
    for i, plate_img in enumerate(plate_imgs):
        plate_img = cv2.resize(plate_img, dsize=(0, 0), fx=1.6, fy=1.6)
        _, plate_img = cv2.threshold(plate_img, thresh=0.0, maxval=255.0,type=cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
        # find contours again (same as above)
        contours, _ = cv2.findContours(plate_img, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)

        plate_min_x, plate_min_y = plate_img.shape[1], plate_img.shape[0]
        plate_max_x, plate_max_y = 0, 0

        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
        
            area = w * h
            ratio = w / h

            if area > MIN_AREA \
            and w > MIN_WIDTH and h > MIN_HEIGHT \
            and MIN_RATIO < ratio < MAX_RATIO:
                if x < plate_min_x:
                    plate_min_x = x
                if y < plate_min_y:
                    plate_min_y = y
                if x + w > plate_max_x:
                    plate_max_x = x + w
                if y + h > plate_max_y:
                    plate_max_y = y + h
                
        img_result = plate_img[plate_min_y:plate_max_y, plate_min_x:plate_max_x]
    
        img_result = cv2.GaussianBlur(img_result, ksize=(3, 3), sigmaX=0)
        _, img_result = cv2.threshold(img_result, thresh=0.0, maxval=255.0, type=cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        img_result = cv2.copyMakeBorder(img_result, top=10, bottom=10, left=10, right=10, borderType=cv2.BORDER_CONSTANT, value=(0,0,0))

        chars = pytesseract.image_to_string(img_result, lang='eng')
        result_chars = ''
        for c in chars:
            if c.isdigit() :
                result_chars += c
        # add the char to the chars plate list 
        plate_chars.append(result_chars)

    serie_detected,reg_detected,s,reg=utils.matching_number(plate_chars)
    if(serie_detected and reg_detected):
        print("---------------------------------------------")
        print("[SUCESS] licence plate detected succesfully :")
        print("[INFO] car number is:%d-%d"%(reg,s))
        t=time.time()-start_time
        print("[INFO] Time Remaining:%d"% t )  
        print("[INFO] Exit Process!")
        break
    else:
        print("---------------------------------------------")
        print("[FAIL] licence plate not detected ! ")
        print("[INFO] processing possible best matched numbers ...")
        print("[INFO] car number is:%d-%d"%(reg,s))
        t=time.time()-start_time
        print("[INFO] Time Remaining:%d"%  t)
   
print("[INFO] end program !")


 
