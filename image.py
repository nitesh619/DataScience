from PIL import Image
import numpy as np
import wave as wv

img = Image.open('thor.jpg')
img = img.convert('L')

arr = np.array(img)
new_arr = arr[0:500,0:500]

img1 = Image.fromarray(new_arr,'L')
img1.show()