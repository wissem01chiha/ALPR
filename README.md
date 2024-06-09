<div align="center">


## Automatic License Plate Recognition 

[![Licence](https://img.shields.io/github/license/wissem01chiha/ALPR)](LICENSE)
![GitHub top language](https://img.shields.io/github/languages/top/wissem01chiha/ALPR)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/wissem01chiha/ALPR)

</div>

### Table of Contents

- [ALPR Package](#project-name)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [General Notes](#general-notes)
  - [Installation](#build)
  - [Usage](#usage)
  - [References](#references)
  - [Contributing](#contributing)
  - [License](#license)


### Description 
ALPR (Automated License Plate Recognition) is a multistage software application designed for the identification and registration of cars' license plates within parking lots or road areas, in both constrained and unconstrained environments

### General Notes
- The project was primarily designed to be integrated within an end-to-end real-time embedded IoT application in public parking areas.
- The package was tested in the development process on [Raspberry-pi-3, Model B+, 2017](cil4sys/doc/raspberry-pi-3-b+.pdf) Before the integration of Yolo v3, you may encounter installation or runtime conflicts. If this happens, please open an issue.
 [issue](https://github.com/wissem01chiha/ALPR/issues)
- Streaming data from the default Raspberry-pi camera module function is not tested, can lead to perfermances issues.
- other embedded platfoms are not testd or supported 
- For C++ devllopers, there is no option to use this version with C or C++.


###  Build and Installation
> **Warning:**  Building OpenCV-lib from source, which is a dependency of the project on Raspberry Pi boards, can fail and consume time. We recommend checking the suitable version of OpenCV for the board and installing the precompiled Python packages for OpenCV listed in the [requirements](requirements.txt)

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

### References
- **Automated License Plate Recognition: A Survey on Methods and Techniques** *J. Shashirangana et al.* **Applied Sciences**, 2020, IEEE.
- **A Robust Real-Time Automatic License Plate Recognition Based on the YOLO Detector** *R. Laroca, E. Severo* **arXiv**, 2018, MDPI.
- **Towards End-to-End Car License Plates Detection and Recognition with Deep Neural Networks** *Hui Li, Peng Wang, and Chunhua Shen* **IEEE**, 2018.
- **Challenges in Automatic License Plate Recognition System: An Indian Scenario** *P. Mukhija, P. K. Dahiya, Priyanka* **IEEE**, 2021.
- **A Comprehensive Review Of Yolo: From Yolov1 And Beyond** *Juan Terven, Diana Margarita Córdova-Esparza* **arXiv**, 2023, MDPI.
- **Automatic License Plate Recognition via Sliding-Window Darknet-YOLO Deep Learning** *Lee, J. S., Su, Y. W., and Shen, C. C.* **Image and Vision Computing**, 2019, Elsevier.
- **RGB to HSI Color Space Conversion via MACT Algorithm** *R. Aruna Jayashree* **International Conference on Communication and Signal Processing**, 2013, India.
- **Blind Estimation of White Gaussian Noise Variance in Highly Textured Images** *M. Ponomarenko, N. Gapon, V. Voronin, K. Egiazarian* **arXiv**, 2017.
- **Realization of the Contrast Limited Adaptive Histogram Equalization (CLAHE) for Real-Time Image Enhancement** *ALI M. REZA* **Journal of VLSI Signal Processing**, 2003.
- **Survey of Smart Parking Systems** *Mathias Gabriel Diaz Ogás* **MDPI**, 2020.
- **Image Denoising Using Wavelet Transform** *Sachin Ruika, D Doye* **ICMET**, 2010.
- **The Unscented Kalman Filter for Nonlinear Estimation** *Wan, Eric A and Van Der Merwe, Rudolph* **Proceedings of the IEEE 2000 Adaptive Systems for Signal Processing, Communications, and Control Symposium (Cat. No. 00EX373)**, 2000.
- **On-Line Smoothing for an Integrated Navigation System with Low-Cost MEMS Inertial Sensors** *Chiang, Kai-Wei et al.* **Sensors**, 2012.
- **Maximum Likelihood Estimates of Linear Dynamic Systems** *Rauch, Herbert E and Tung, F and Striebel, Charlotte T* **AIAA Journal**, 1965.


### Contributing
---
Please see first the [CHANGELOG](CHANGELOG.md) guide.  

Feel free to mail to :  
- chihawissem08@gmail.com 
#### Contributors

<a href="https://github.com/wissem01chiha/ALPR/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=wissem01chiha/ALPR" />
</a>


 
### License
---
This project is actually under The GNU General Public License.  
 See the [LICENCE](LICENCE) file for more details.    









 










 

[installation]: #installation
