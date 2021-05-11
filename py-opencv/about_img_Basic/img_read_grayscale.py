import cv2 as cv

path = # img path

img = cv.imread(path, cv.IMREAD_GRAYSCALE)

if img is None:
    print('image load failed')
    exit()

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()