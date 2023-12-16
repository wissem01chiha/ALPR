# run_cil4sys.py
    # This script is meant to be run from the command line by the user.
    # It parses command-line arguments using the argparse module.
    # It imports functions or modules from other files (like main_module.py) to perform specific tasks.
import argparse
import os
from cil4sys import main

parser = argparse.ArgumentParser(
                prog='ALPR',
                description='ALPR: Automated License Plate Tracker tracks car and extract license plate number from live/recorded video',
                epilog='Text at the bottom of help'
                )
                    
def valide_file(choices,fname):
    ext = os.path.splitext(fname)[1][1:]
    if ext not in choices:
       parser.error("file doesn't end with one of {}".format(choices))
    return fname
  

def parse_args():
    # Add the optional argument for the recorded video file path
    parser.add_argument('-v','--video',
                          dest="video_path",
                          help='Path to the recorded video file',
                          type=lambda s:valide_file(("mp4","avi"),s), #str
                          default= None,
                          required=False
                          )
    return parser.parse_args()



def main_cli():
    args = parse_args()
    video_path = args.video_path

    # Call the main function from main.py
    main(video_path)


if __name__ == "__main__":

    #args = parse_args()
    # Assign the video_path variable based on the command line argument
    #video_path = args.video_path
    # Call the main function with the provided video path
    #main(video_path=args.video_path)
    main_cli()
