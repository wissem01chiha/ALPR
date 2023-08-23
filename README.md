##  Car Licencing Plate Detection and Recognition  Embedded Software for Intelligent Parking Systems.




### Table of Contents

- [LPDR Embedded Software](#project-name)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Features](#features)
  - [Build](#Build)
  - [Installation][installation]
  - [Usage](#usage)
  - [Documentation](#documentation)
  - [Contributing](##contributing)
  - [License](#license)
  - [Contact](#contact)
  - [Acknowledgments](#acknowledgments)

### Description 
LPDR (License Plate Detection and Registration) is an automated application designed to identify and register car license plates within parking areas.  

 The primary function of LPDR involves the detection of license plates, which are subsequently recorded for billing purposes.  
This application employs a multi-stage approach, utilizing both video and image processing techniques, to accurately extract 

Tunisian license plate numbers. However, it's important to note that the current version of LPDR is limited to recognizing numerical characters on license plates and does not have the capability to read non-numerical characters. 
### Features 
- Processing of video records  from the parking camera
- License Plate Detection: Utilizes computer vision techniques to accurately locate license plates in various conditions.
- Optical Character Recognition (OCR): Recognizes alphanumeric characters on license plates, converting visual data to readable text.



###  Installation

Update package information and upgrade installed packages

        sudo apt update
        sudo apt upgrade

Upgrade Python packages: pip, setuptools, and wheel

        pip install --upgrade pip setuptools wheel

Install library dependencies 

    sudo apt install libatlas-base-dev gfortran
    sudo apt install python3-opencv libopencv-dev

clone to the repository 

    git clone https://github.com/wissem01chiha/cil4sys

Navigate to the repository's dist folder and run 

    pip3  install ./dist/cil4sys-0.1.tar.gz

This will install the application with it dependencies and data files.  

Verify the installation 

    cil4sys --version

### Build   
Standlone compiled binaries are can be found at dist folder , for raspberry pi  platform 

Install pyinstller on rasberry pi 

    sudo pip3 install pyinstaller  

Install the code package with commands in  [Installation][installation]

run   

    pyinstaller main.py

### Usage
The application provide 
run  the main.py script 
### Documentation 

![Local Image](doc/wiring.png)


1. Start
2. Record video 
3. Split and Sample video frames. 
4. Detect motioned regions.
5. Crop regions of intrest.
6. Enhance ROI Contrast. 
7. Sort images:
    - Proportion of white and black color
8. Filtre result images:  
    - SSIM index      : remove similar regions images
    - Estimate noise  : using DCT transform  
    - SNR index       : select best noisless images
9. Adjust images saturation
    - HSI transform 
10. Image segmentation (thresholding)
11. Find Countours.
12. Select Countours By: 
      - Char size
      - Arrangement
13. Rotate Plate Images
14. Extract numbers with OCR
15. Get possible LP numbers with fazzy logic 
    algorithm (not fully implemented)
16. end 


#### Package Architecture
### Contributing 
### License
this is under 
### Contact
### Acknowledgments









 










 

[installation]: #installation
