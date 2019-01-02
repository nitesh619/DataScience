import cv2

image = cv2.imread('shape.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, ksize=5)
# cv2.imshow('gray', gray)
# cv2.waitKey(0)

edge = cv2.Canny(blur, 50, 200)
# cv2.imshow('edge', edge)
# cv2.waitKey(0)
contour, _ = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(image, [contour], -1, (0, 0, 0), 4)
cv2.imshow('iamge', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
