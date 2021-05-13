import numpy as np
import cv2 as cv

canvas = np.full((200,600,3), 255, np.uint8)

string = 'example string'
fontFace = cv.FONT_HERSHEY_SIMPLEX
fontScale = 2.0
thickness = 1

sizeText, _ = cv.getTextSize(string, fontFace, fontScale, thickness)

org = ((canvas.shape[1] - sizeText[0])//2, (canvas.shape[0] + sizeText[1])//2)
cv.putText(canvas, string, org, fontFace, fontScale, (255,0,0), thickness)

cv.rectangle(canvas, org,(org[0]+sizeText[0], org[1]-sizeText[1]), (0,255,0),1)

cv.imshow("canvas", canvas)
cv.waitKey()
cv.destroyAllWindows()