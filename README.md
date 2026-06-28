NEF to JPG Converter

A simple Python script that converts NEF (Nikon RAW) images to JPG format.

Features
Converts all .nef files from a source folder.
Saves the converted .jpg files to a destination folder.
Easy to configure.

Configuration
Before running the script, open the Python file and update the folder paths:

In code replace these paths with:

input_folder = r"input folder path"  
output_folder = r"output folder path"

Usage:

This project requires Python 3 and the following libraries:
pip install rawpy imageio

Run:
python converter.py
