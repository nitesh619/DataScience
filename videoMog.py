import cv2

cap = cv2.VideoCapture('UP.mp4')
doctor = cv2.VideoCapture('DS.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
while (1):
    ret, frame = cap.read()
    _, doc = doctor.read()

    frame = cv2.resize(frame, (720,304))
    rows, cols, channels = frame.shape
    roi = doc[0:rows, 0:cols]

    logo_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # ret, mask = cv2.threshold(logo_gray, 80, 255, cv2.THRESH_BINARY_INV)
    mask = fgbg.apply(frame)
    mask_inv = cv2.bitwise_not(mask)

    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    logo_fg = cv2.bitwise_and(frame, frame, mask=mask)

    doc[0:rows, 0:cols] = cv2.add(img1_bg, logo_fg)
    cv2.imshow('mask', doc)

    # fgmask = fgbg.apply(frame)
    # cv2.imshow('frame', fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
doctor.release()
cv2.destroyAllWindows()
