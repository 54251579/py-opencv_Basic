import cv2 as cv
import numpy as np

path = # video path

cap = cv.VideoCapture(path)
if not cap.isOpened():
    print('video open failed')
    exit()

print('frame width:', int(cap.get(cv.CAP_PROP_FRAME_WIDTH)))
print('frame height:', int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
print('frame count:', int(cap.get(cv.CAP_PROP_FRAME_COUNT)))

fps = cap.get(cv.CAP_PROP_FPS)
print('fps: ', fps)
delay = round(1000/fps)

while True:
    _, frame = cap.read()
    
    if not _:
        break

    inversed = ~frame

    cv.imshow('frame', frame)
    cv.imshow('inversed', inversed)

    if cv.waitKey(delay) == 27:
        break

cv.destroyAllWindows()
