import cv2

img = cv2.imread('open_CV.png', cv2.IMREAD_COLOR)

# nm_arr = np.zeros_like(img)
# new = np.dstack([img[:, :, 2], nm_arr])
print(img)
red_cv = img[30:140, 130:260]
img[0:110,0:130] = red_cv
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
