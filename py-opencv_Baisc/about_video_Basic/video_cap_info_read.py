import cv2 as cv
import sys

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print('camera open failed')
    sys.exit()

print('frame width: ', int(cap.get(cv.CAP_PROP_FRAME_WIDTH)))
print('frame height: ', int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))