import cv2 as cv
import numpy as np
import sys

old_x, old_y = 0, 0

def on_mouse(event, x, y, flags, param):
    global old_x, old_y

    if event == cv.EVENT_LBUTTONDOWN:
        old_x, old_y = x, y
        print(f'EVENT_LBUTTONDOWN: {x}, {y}')
    elif event == cv.EVENT_LBUTTONUP:
        print(f'EVENT_LBUTTONUP: {x}, {y}')

    elif event == cv.EVENT_MOUSEMOVE:
        if flags & cv.EVENT_FLAG_LBUTTON:
            cv.line(canvas, (old_x, old_y), (x,y), (0,255,0), 2)
            cv.imshow('canvas', canvas)
            old_x ,old_y = x, y

canvas = np.full((400, 400, 3), 255, np.uint8)

cv.namedWindow('canvas')
cv.setMouseCallback('canvas', on_mouse)

cv.imshow('canvas', canvas)
cv.waitKey(0)
cv.destroyAllWindows()