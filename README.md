<div align="center">

## Car Licensing Plate Detection and Recognition Project 

[![Licence](https://img.shields.io/github/license/wissem01chiha/ALPR)](LICENSE)
![GitHub top language](https://img.shields.io/github/languages/top/wissem01chiha/ALPR)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/wissem01chiha/ALPR)

</div>

### Table of Contents

- [ALPR Package](#project-name)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Features](#features)
  - [Installation](#build)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)


### Description 
ALPR (Automated License Plate Detection and Registration) is an automated application designed to identify and register car license plates within parking areas.  

 The primary function of the application is the detection of license plates, which are subsequently recorded for billing purposes.  
This application employs a multi-stage approach, utilizing both video and image processing techniques, to accurately extract 

Tunisian license plate numbers. However, it's important to note that the current version of LPDR is limited to recognizing numerical characters on license plates and does not have the capability to read non-numerical characters. 
### Features 
- Processing of video records  from the parking camera
- License Plate Detection: Utilizes computer vision techniques to accurately locate license plates in various conditions.
- Optical character recognition : Recognizes alphanumeric characters on license plates, converting visual data to readable text.


###  Build and Installation
#### Build 
To build the package using python setuptools run :  

    python setup.py sdist --dist-dir build

It will generate a distributable version under the build/ directory. 

or with :

    python -m build 

to get a *.tar.gz and *.whl files under the  dist/ diractory. 
#### Installation on Raspberry pi Board 

Update package information and upgrade installed packages

        sudo apt update
        sudo apt upgrade

Upgrade Python packages: pip, setuptools, and wheel

    pip install --upgrade pip setuptools wheel

Install library dependencies 

    sudo apt install python3-opencv libopencv-dev

clone to the repository 

    git clone git@github.com:wissem01chiha/ALPR.git

Navigate to the repository  folder and run 

    pip3  install ./dist/cil4sys-0.1.1.tar.gz

This will install the application with it dependencies and data files.  

 
### Usage

connect your camera to raspberry pi board throgh the USB port or the default raspiberry port, only one camera wich is ste to default will be detected  for the raspi kit camera you miust enable the camera interface 

after installation navigate to the main script diractory folder and run :

    python3 main.py 
 
### Contributing
Please see the [contributing](CONTRIBUTING.md) guide.
 
 
#### Contributors

<a href="https://github.com/wissem01chiha/ALPR/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=wissem01chiha/ALPR" />
</a>


Please feel free to mail to:  
- chihawissem08@gmail.com  
### License
This project is actually under The GPL licence. See the [License](LICENCE) file for more details.    









 










 

[installation]: #installation
