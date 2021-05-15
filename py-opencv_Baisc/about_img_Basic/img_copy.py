import cv2 as cv
import numpy as np

path = # img path

img = cv.imread(path)

if img is None:
    print('image load failed')
    exit()

print(type(img))
print(img.shape)

if len(img.shape) == 2:
    print('graay scale')
elif len(img.shape) == 3:
    print('true color')

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()