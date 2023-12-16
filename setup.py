import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cil4sys",
    version="0.1.2",
    author="Wissem Chiha",
    author_email="chihawissem@gmail.com",
    description="LPDR package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wissem01chiha/cil4sys",
    packages=setuptools.find_packages(),
    package_data={'config': ['*.json','*.sh'],'data':['videos/*.mp4']},
    py_modules=["main"],
    install_requires=[
        "multiprocess==0.70.15",
        "numpy==1.23.5",
        "opencv_python==4.6.0.66",
        "Pillow==10.0.0",
        "pytesseract==0.3.10",
        "scipy==1.8.1",
        "setuptools==68.1.2",
        "scikit-image==0.18.1"
    ],
    entry_points={
        'console_scripts': [
            'run_cil4sys = cil4sys.run_cil4sys:main',
        ],
    },
    
    )
