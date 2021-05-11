import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print('camera open failed')
    exit()

print('frame width: ', int(cap.get(cv.CAP_PROP_FRAME_WIDTH)))
print('frame height: ', int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))