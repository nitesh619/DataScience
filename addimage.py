import numpy as np
import cv2

batman = cv2.imread('batman.jpg')
thor = cv2.imread('thor.jpg')

##different ways to add
mix = thor + batman
cv2_mix = cv2.add(thor, batman)
weighted = cv2.addWeighted(batman, 0.7, thor, 0.3, 0)

cv2.imshow('mix', weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()