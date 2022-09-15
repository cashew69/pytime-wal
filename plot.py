import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
file = ""
with Image.open(file) as im:
    im = im.convert('L')
    data = list(im.getdata())
plt.hist(data, bins = int(180/5),edgecolor = 'black')
plt.show()

