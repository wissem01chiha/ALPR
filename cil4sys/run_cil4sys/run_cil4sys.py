#!/usr/bin/python3

# run_cil4sys.py
    # This script is meant to be run from the command line by the user.
    # It parses command-line arguments using the argparse module.
    # It imports functions or modules from other files (like main_module.py) to perform specific tasks.
import argparse
import os
import pkg_resources
from cil4sys import main


                    
def valide_file(choices, fname):
    if not os.path.exists(fname):
        raise argparse.ArgumentTypeError(f"File '{fname}' does not exist.")
    
    ext = os.path.splitext(fname)[1][1:]
    if ext.lower() not in choices:
        raise argparse.ArgumentTypeError(f"File must have one of the following extensions: {', '.join(choices)}")
    return fname
  

def parse_args():
    parser = argparse.ArgumentParser(
                  prog='ALPR',
                  description='ALPR: Automated License Plate Tracker tracks car and extract license plate number from live/recorded video',
                  epilog='Text at the bottom of help'
                  )
    # Add the optional argument for the recorded video file path
    parser.add_argument('-v','--video',
                          dest="video_path",
                          help='Path to the recorded video file',
                          type=lambda s:valide_file(("mp4","avi"),s), #str
                          #default= None,
                          required=False
                          )
    return parser.parse_args()



def main_cli():
    args = parse_args()
    #print(f"[ARG] {args}")  # Add this line to print the parsed arguments
    video_path = args.video_path

    # Get the directory of the current script
    #script_directory = os.path.dirname(os.path.abspath(__file__))
    # Get the directory of the installed package
    #package_directory = os.path.dirname(pkg_resources.resource_filename(__name__, ''))
    #print(f"package directory:{package_directory}")

    # Construct the full video path
    #full_video_path = os.path.join(package_directory, video_path) if video_path else video_path

    #print(f"Video Path: {full_video_path}")

    # Call the main function from main.py
    main(video_path=video_path)
    pass



if __name__ == "__main__":

    #args = parse_args()
    # Assign the video_path variable based on the command line argument
    #video_path = args.video_path
    # Call the main function with the provided video path
    #main(video_path=args.video_path)
    main_cli()
