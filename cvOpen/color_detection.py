import urllib.request

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
kernel = np.ones((5, 5), np.uint8)


def showContours(contours, res, text):
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            x, y, w, h = cv2.boundingRect(contour)
            res = cv2.rectangle(res, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(res, text, (x + 10, y + 44), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))


while True:
    # _, frame = cap.read()
    ip_image = urllib.request.urlopen('http://192.168.0.100:8080/shot.jpg')
    ip_np_arr = np.array(bytearray(ip_image.read()), dtype=np.uint8)

    ip = cv2.imdecode(ip_np_arr, -1)
    frame = cv2.resize(ip, None, fx=.5, fy=.5, interpolation=cv2.INTER_CUBIC)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # ssc = cv2.pyrMeanShiftFiltering(hsv,31,91)

    blue_lower = np.array([110, 50, 50])
    blue_upper = np.array([120, 255, 255])

    yellow_lower = np.array([22, 60, 200])
    yellow_upper = np.array([60, 255, 255])

    red_lower = np.array([136, 87, 111])
    red_upper = np.array([180, 255, 255])

    white_lower = np.array([136, 87, 111])
    white_upper = np.array([180, 255, 255])

    mask_yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
    mask_red = cv2.inRange(hsv, red_lower, red_upper)
    mask_blue = cv2.inRange(hsv, blue_lower, blue_upper)
    mask_1 = cv2.bitwise_or(mask_yellow, mask_blue)

    mask = cv2.bitwise_or(mask_1, mask_red)
    dilate = cv2.dilate(mask, kernel)
    res = cv2.bitwise_and(frame, frame, mask=dilate)

    _, red_contours, hierarchy1 = cv2.findContours(mask_red, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    _, blue_contours, hierarchy2 = cv2.findContours(mask_blue, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    _, yellow_contours, hierarchy3 = cv2.findContours(mask_yellow, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    showContours(red_contours, frame, 'RED')
    showContours(blue_contours, frame, 'BLUE')
    showContours(yellow_contours, frame, 'YELL')

    cv2.imshow('original', frame)

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
