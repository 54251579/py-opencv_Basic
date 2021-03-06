import cv2 as cv
import sys

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print('camera open failed')
    sys.exit()

frame_rate = 33
while True:
    _, frame = cap.read()
    if not (_):
        break

    cv.imshow('frame', frame)
    
    key = cv.waitKey(frame_rate)
    if key == 27:
        break

if cap.isOpened():
    cap.release()
cv.destroyAllWindows()