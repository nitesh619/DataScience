import urllib.request

import cv2
import numpy as np

while True:
    ip_image = urllib.request.urlopen('http://192.168.0.100:8080/shot.jpg')
    ip_np_arr = np.array(bytearray(ip_image.read()), dtype=np.uint8)

    ip = cv2.imdecode(ip_np_arr, -1)
    res = cv2.resize(ip, None, fx=.5, fy=.5, interpolation=cv2.INTER_CUBIC)
    cv2.imshow("IP image", res)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cv2.destroyAllWindows()
