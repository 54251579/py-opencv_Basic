import cv2 as cv
import sys

path = # img path

img = cv.imread(path)

if img1 is None:
    print('image load failed')
    sys.exit()

img2 = img1
img3 = img1.copy()

img1[:, :] = (0,255,255)  # BGR

cv.imshow('img1', img1)
cv.imshow('img2', img2)
cv.imshow('img3', img3)

cv.waitKey(0)
cv.destroyAllWindows()