import cv2

img1 = cv2.imread('wal\\nEX1YC1.jpg')
logo = cv2.imread('spLogo.jpg')

rows, cols, channels = logo.shape
roi = img1[0:rows, 0:cols]

logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(logo_gray, 210, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
logo_fg = cv2.bitwise_and(logo, logo, mask=mask)


img1[0:rows, 0:cols] = cv2.add(img1_bg, logo_fg)
cv2.imshow('mask', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
