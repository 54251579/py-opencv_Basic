import cv2 as cv
import sys

path = './img/Lenna.png'
img = cv.imread(path)
if img is None:
    print('img load failed')
    sys.exit()

