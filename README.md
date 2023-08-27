##  Car Licencing Plate Detection and Recognition  Embedded Software for Intelligent Parking Systems.

![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)
![json](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white )
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![numba](https://img.shields.io/badge/Numba-00A3E0?style=for-the-badge&logo=Numba&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white)
![Raspberrypi](https://img.shields.io/badge/Raspberry%20Pi-A22846?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white)



### Table of Contents

- [LPDR Embedded Software](#project-name)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Features](#features)
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

#### installation on Raspberry pi Board 

Update package information and upgrade installed packages

        sudo apt update
        sudo apt upgrade

Upgrade Python packages: pip, setuptools, and wheel

        pip install --upgrade pip setuptools wheel

Install library dependencies 

    sudo apt install python3-opencv libopencv-dev

clone to the repository 

    git clone https://github.com/wissem01chiha/cil4sys

Navigate to the repository  folder and run 

    pip3  install ./dist/cil4sys-0.1.tar.gz

This will install the application with it dependencies and data files.  

To check that all software modules are installed : 




### Usage

connect your camera to raspberry pi board throgh the USB port or the default raspi port , only one camera wich is ste to default will be detected  for the raspi kit camera you miust enable the camera interface 

after installation navigate to the main script diractory folder and run 

    python main.py 
 
### Documentation 



### Contributing 

### License
This project is actually under The GNU licence,   
### Contact
chihawissem08@gmail.com  

### Acknowledgments

<img src="doc/cil4sys_logo.png" alt="Local Image" width="210" height="100">







 










 

[installation]: #installation
