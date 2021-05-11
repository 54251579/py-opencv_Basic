import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print('camera open failed')
    exit()

frame_rate = 33
while True:
    _, frame = cap.read()
    if not (_):
        break
    
    inversed = ~frame

    cv.imshow('frame', frame)
    cv.imshow('inversed', inversed)
    
    key = cv.waitKey(frame_rate)
    if key == 27:
        break

if cap.isOpened():
    cap.release()
cv.destroyAllWindows()