# Image Format Conversion

These scripts allow you to convert images between PNG and JPG formats.

## Prerequisites

Required Modules:
- PIL==1.1.6

To install the necessary modules, run the following command:
```
$ pip install -r requirements.txt
```

## Running the Scripts

### Dynamic Format Change
To dynamically convert all JPG images to PNG and PNG images to JPG in the current directory and its subdirectories, follow these steps:

1. Copy the `convertDynamic.py` script to the directory where your images are located.
2. Run the following command:
   ```bash
   $ python convertDynamic.py
   ```

### JPG to PNG (Single Image)
To convert a single JPG image to PNG format, perform the following steps:

1. Copy the JPG image to the directory where the `JPGtoPNG.py` script is located.
2. Replace the file name `naruto_first.jpg` inside `JPGtoPNG.py` (line 3) with the input file name (JPG).
3. Replace the file name `naruto.png` inside `JPGtoPNG.py` (line 4) with the output file name (PNG).
4. Run the following command:
   ```
   $ python JPGtoPNG.py
   ```

### PNG to JPG (Single Image)
To convert a single PNG image to JPG format, follow these steps:

1. Copy the PNG image to the directory where the `PNGtoJPG.py` script is located.
2. Replace the file name `naruto_first.png` inside `PNGtoJPG.py` (line 3) with the input file name (PNG).
3. Replace the file name `naruto.jpg` inside `PNGtoJPG.py` (line 4) with the output file name (JPG).
4. Run the following command:
   ```
   $ python PNGtoJPG.py
   ```