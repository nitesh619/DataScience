import cv2

batman = cv2.imread('batman.jpg')
thor = cv2.imread('thor.jpg', 0)

##different ways to add
print(thor.shape)
# mix = thor + batman
# cv2_mix = cv2.add(thor, batman)
# weighted = cv2.addWeighted(batman, 0.7, thor, 0.3, 0)

cv2.imshow('mix', thor.T)
cv2.waitKey(0)
cv2.destroyAllWindows()