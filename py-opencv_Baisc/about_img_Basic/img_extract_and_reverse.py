import cv2 as cv
import sys

path = # img path

img1 = cv.imread(path)

if img1 is None:
    print('image load failed')
    sys.exit()

img2 = img1[200:400, 200:400]
img3 = img1[200:400, 200:400].copy()

img2 += 20

cv.imshow('img1', img1)
cv.imshow('img2', img2)
cv.imshow('img3', img3)

cv.waitKey(0)
cv.destroyAllWindows()