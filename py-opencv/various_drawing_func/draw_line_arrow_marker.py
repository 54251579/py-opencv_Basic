import numpy as np
import cv2 as cv

canvas = np.full((400, 400, 3), 255, np.uint8)

cv.line(canvas, (50, 50), (200, 50), (0, 0, 255))
cv.line(canvas, (50, 100), (200, 100), (255, 0, 255), 3)
cv.line(canvas, (50, 150), (200, 150), (255, 0, 0), 10)

cv.line(canvas, (250, 50), (350, 100), (0, 0, 255), 1, cv.LINE_4)
cv.line(canvas, (250, 70), (350, 120), (255, 0, 255), 1, cv.LINE_8)
cv.line(canvas, (250, 90), (350, 140), (255, 0, 0), 1, cv.LINE_AA)

cv.arrowedLine(canvas, (50, 200), (150, 200), (0, 0, 255), 1)
cv.arrowedLine(canvas, (50, 250), (350, 250), (255, 0, 255), 1)
cv.arrowedLine(canvas, (50, 300), (350, 300), (255, 0, 0), 1, cv.LINE_8, 0, 0.05)

cv.drawMarker(canvas, (50, 350), (0, 0, 255), cv.MARKER_CROSS)
cv.drawMarker(canvas, (100, 350),  (0, 0, 255), cv.MARKER_TILTED_CROSS)
cv.drawMarker(canvas, (150, 350),  (0, 0, 255), cv.MARKER_STAR)
cv.drawMarker(canvas, (200, 350), (0, 0, 255), cv.MARKER_DIAMOND)
cv.drawMarker(canvas, (250, 350),  (0, 0, 255), cv.MARKER_SQUARE)
cv.drawMarker(canvas, (300, 350),  (0, 0, 255), cv.MARKER_TRIANGLE_UP)
cv.drawMarker(canvas, (350, 350),  (0, 0, 255), cv.MARKER_TRIANGLE_DOWN)

cv.imshow('canvas', canvas)
cv.waitKey()
cv.destroyAllWindows()