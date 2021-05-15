import cv2 as cv
import numpy as np

def value_change(value):
    canvas[:] = value
    cv.imshow('canvas', canvas)

canvas = np.zeros((500,500), np.uint8)

cv.namedWindow('canvas')
cv.createTrackbar('value', 'canvas', 0, 255, value_change)

cv.imshow('canvas', canvas)
cv.waitKey()
cv.destroyAllWindows()