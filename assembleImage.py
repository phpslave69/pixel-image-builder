from PIL import Image
import numpy as np
from numpy import asarray
import const

f = open("pixels/img_res.txt", "r")
cfg = open("pixels/cfg.txt", "r")



pixels = []

for textLine in f:
    pixels.append([int(x) for x in textLine.replace("\n", "").split(" ")])
   

for textLine in cfg:
    width = int(textLine)


matrix = np.array([pixels[i:i + width] for i in range(0, len(pixels), width)])

image2 = Image.fromarray(matrix.astype('uint8'), 'RGB')
image2.save("images/result.png")