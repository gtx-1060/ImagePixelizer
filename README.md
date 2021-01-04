<h1 align="center">
  <br>
  <a href="https://github.com/gtx-1060/ImagePixelizer"><img src="https://i.ibb.co/B37rSdy/Frame-1.png" alt="ImagePixelizer "></a>
  <br>
  ImagePixelizer 
  <br>
</h1>
<p align="center">Python script for pixelating pictures using <a href="https://pixel-me.tokyo/en/">pixel-me</a> API</p>

## Features
 - You can adjust the strength of pixelation
 - Works in multithreaded mode
 - Can processes an unlimited number of images per approach
 - Configuration file for options
 
 
## Compatibility
Check your Python version by typing in
```shell script
python --version
```
If you get the following
```shell script
Python 3.7.*
```
this script has been tested and confirmed to be supported.


## Usage
1. Go to the project folder and type in the console
```shell script
pip install -r requirements.txt
```
2. Then open *config.json* file and write path to images and output path.
```
{
    "sources_path" : "YOUR PATH TO FOLDER WITH IMAGES HERE",
    "output_path" :  "YOUR PATH TO OUTPUT FOLDER HERE"
}
```
Then just execute *launcher.py* script.

## Attention!
- Don't forget the slashes at the end of the pathes
- Use '/' or '\\' (on windows) in the pathes (not one backslash )
