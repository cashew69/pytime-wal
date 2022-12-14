import numpy as np
import shutil
import os
from PIL import Image

def how_bright(intensity, x):
    if intensity < 50:
        shutil.move(path + x ,'wallpapers/4/')
    elif intensity < 100:
        shutil.move(path + x ,'wallpapers/3/')
    elif intensity < 155:
        shutil.move(path + x ,'wallpapers/2/')
    elif intensity < 255:
        shutil.move(path + x ,'wallpapers/1/')


path = "wallpapers/download/"
files = os.listdir(path)
files = list(files)
for x in files:
    with Image.open(path+x) as im:
        im = im.convert('L')
        data = list(im.getdata())

    omean=np.mean(data)
    oSD=np.std(data)
    final_list = [x for x in data if (x > omean - 0.5 * oSD)]
    final_list = [x for x in final_list if (x < omean + 0.5 * oSD)]
    mean=np.mean(final_list)
    SD=np.std(final_list)
    how_bright(mean, x)


print("DONE")

