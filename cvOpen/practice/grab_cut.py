import cv2
import numpy as np

# cap = cv2.VideoCapture(0)
# img1 = cv2.imread('wal\\nEX1YC1.jpg')
# nitesh = None
# while (True):
#     _, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     nitesh = frame
#     cv2.imshow('image', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# When everything done, release the capture

# cap.release()
# cv2.destroyAllWindows()

nitesh = cv2.imread('nitesh.jpg')
mask = np.zeros(nitesh.shape[:2], np.uint8)

bgModel = np.zeros((1, 65), np.float64)
fgModel = np.zeros((1, 65), np.float64)
rect = (270, 66, 270, 340)
cv2.grabCut(nitesh, mask, rect, bgModel, fgModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 1), 0, 1).astype('uint8')
nitesh = nitesh * mask2[:, :, np.newaxis]

cv2.imshow('rand', mask2)
cv2.waitKey(0)
cv2.destroyAllWindows()
