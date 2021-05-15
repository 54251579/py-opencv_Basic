import cv2 as cv
import sys

path = # img path

img = cv.imread(path)

if img is None:
    print('image load failed')
    sys.exit()

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()