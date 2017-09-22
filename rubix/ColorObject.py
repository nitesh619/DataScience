import cv2
import numpy as np


class ColorObject(object):
    kernel = np.ones((5, 5), np.uint8)

    def __init__(self, color, color_lower, color_upper):
        self.color = color
        self.color_lower = np.array(color_lower)
        self.color_upper = np.array(color_upper)

    def get_color_mask(self, image_hsv):
        mask = cv2.inRange(image_hsv, self.color_lower, self.color_upper)
        dilate_mask = cv2.dilate(mask, ColorObject.kernel)
        return dilate_mask

    def getColorContours(self, image_hsv):
        mask = self.get_color_mask(image_hsv)
        return cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[1]

    def drawDetectedObjects(self, image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        color_objects = self.getColorContours(hsv)
        for obj in color_objects:
            area = cv2.contourArea(obj)
            if area > 500:
                x, y, w, h = cv2.boundingRect(obj)
                image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 0), 2)
                cv2.putText(image, self.color, (x + 10, y + 44), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0))


if __name__ == "__main__":
    print("color object detection")
