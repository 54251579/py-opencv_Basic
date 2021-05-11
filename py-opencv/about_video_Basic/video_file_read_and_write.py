import cv2 as cv

path = # video path

cap = cv.VideoCapture(path)

if not cap.isOpened():
    print('video open failed')
    exit()

width = round(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv.CAP_PROP_FPS)

fourcc = cv.VideoWriter_fourcc(*'DIVX')
delay = round(1000/fps)

out_put_video = cv.VideoWriter('output.avi', fourcc, fps, (width, height))

if not out_put_video.isOpened():
    print('file open failed')
    exit()

while True:
    
    _, frame = cap.read()

    if not (_):
        break

    inversed = ~frame
    out_put_video.write(inversed)
    cv.imshow('frame', frame)
    cv.imshow('inversed', inversed)

    if cv.waitKey(delay) == 27:
        break

cv.destroyAllWindows()