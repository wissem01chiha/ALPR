import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cil4sys",
    version="0.1",
    author="Wissem Chiha",
    author_email="chihawissem@gmail.com",
    description="LPDR package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wissem01chiha/cil4sys",
    packages=setuptools.find_packages(),
    py_modules=["main"],
    install_requires=[
        "multiprocess==0.70.15",
        "numpy==1.23.5",
        "opencv_python==4.5.5.62",
        "Pillow==10.0.0",
        "pytesseract==0.3.10",
        "scipy==1.6.0",
        "setuptools==68.1.2",
        "scikit-image==0.18.1"
    ],
    
    )