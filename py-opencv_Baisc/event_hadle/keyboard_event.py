import cv2 as cv
import sys

path = # img path
img = cv.imread(path)
if img is None:
    print('img load failed')
    sys.exit()

cv.namedWindow('img')
cv.imshow('img', img)

while True:
    key = cv.waitKey()
    if key == ord('I') or key == ord('i'):
        img = ~img
        cv.imshow('img', img)
    elif key == ord('Q') or key == ord('q'):
        break

cv.destroyAllWindows()
