import cv2

import ColorObject as cod

image = cv2.imread('colors.jpg')
blueDetector = cod.ColorObject('Blue', [110, 50, 50], [120, 255, 255])
redDetector = cod.ColorObject('Red', [170, 200, 100], [180, 255, 255])
greenDetector = cod.ColorObject('Green', [45, 100, 100], [75, 255, 200])
yellowDetector = cod.ColorObject('yell', [25, 150, 240], [35, 255, 255])
orangeDetector = cod.ColorObject('org', [10, 150, 220], [20, 255, 255])

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
g_mask = orangeDetector.get_color_mask(hsv)

print(len(yellowDetector.getColorContours(hsv)))

blueDetector.drawDetectedObjects(image)
redDetector.drawDetectedObjects(image)
greenDetector.drawDetectedObjects(image)
yellowDetector.drawDetectedObjects(image)
orangeDetector.drawDetectedObjects(image)

cv2.imshow('mask', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
