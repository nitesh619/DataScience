import numpy as np
from PIL import Image

img = Image.open('digits.png').convert('L')

img_arr = np.array(img)
for r in np.vsplit(img_arr, 50):
    # print(r,end='*')
    for j in r:
        x = np.hsplit(j, 100)

cells = [np.hsplit(row, 100) for row in np.vsplit(img_arr, 50)]

x = np.array(cells)
print('---------------------')
print(x.shape)
print(x[13, 99, :, :], "\n")
img1 = Image.fromarray(x[33, 99, :, :], 'L')
show = img1.show()
# print(x[30,99,:,:], "\n")
# print(x[23,99,:,:], "\n")
# train = x[:,:50].reshape(-1,400).astype(np.float32) # Size = (2500,400)
# test = x[:,50:100].reshape(-1,400).astype(np.float32) # Size = (2500,400)#
