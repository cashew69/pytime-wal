### pytime-wal

In this project "image_classifer.py" file sorts downloaded images.
Images are sorted as per the quantity of dark and non-dark pixels in image. 

+ Put your wallpapers in wallpapers/download/ directiory.

##### Run
python3 image_classifer.py

+ walit is shell script that can be used to set wallpaper.
+ walit look for time by executing date +'%H' command, and sets the wallpaper as per time value.
+ learn more about date from "man date"
+ walit uses pywal for desktop wallpaper setup.
+ 'wal -i' can be replaced by other command.
##### Run
./walit

+ plot.py can be used to visualize distribution of pixels.
+ plot.py does not serve any purpose in actual program.

##### Dependencies
numpy
shutil
os
PIL (pillow image processing)

###### Optional
matplotlib (used by plot.py)
pywal (used by walit)
// For wallpaper setup lightweight programs such as fehbg, hsetroot, xsetroot.
