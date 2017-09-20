import cv2
import numpy as np

cap = cv2.VideoCapture(0)
kernel = np.ones((2, 2), np.uint8)

while True:
    _, frame = cap.read()
    ssc = cv2.pyrMeanShiftFiltering(frame,31,91)
    grey = cv2.cvtColor(ssc, cv2.COLOR_BGR2GRAY)

    _, thrs = cv2.threshold(grey, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    im2, contours, hierarchy = cv2.findContours(thrs, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (255, 255, 255), 3)
    print(len(contours))
    cv2.imshow('original', thrs)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

# smoth = cv2.filter2D(res, -1, kernel)
# blur = cv2.GaussianBlur(res, (15, 15), 0)
# median = cv2.medianBlur(res, 15)
# dialation = cv2.dilate(mask, kernel, iterations=1)
# opening = cv2.morphologyEx(mask_blue, cv2.MORPH_OPEN, kernel)
# closing = cv2.morphologyEx(mask_blue, cv2.MORPH_CLOSE, kernel)
