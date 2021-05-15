import numpy as np
import cv2 as cv

json_filename = 'img/save_img/data.json'
yaml_filename = 'img/save_img/data.yml'
xml_filename = 'img/save_img/data.xml'

def read(filename):
    fs = cv.FileStorage(filename, cv.FILE_STORAGE_READ)

    if not fs.isOpened():
        print('file open failed')
        return
    
    name = fs.getNode('name').string()
    age = int(fs.getNode('age').real())
    pt1 = tuple(fs.getNode('point').mat().astype(np.int32).flatten())
    scoures = tuple(fs.getNode('scores').mat().flatten())
    mat1 = fs.getNode('data').mat()

    fs.release()

    print(name)
    print(age)
    print(pt1)
    print(scoures)
    print(mat1)

read(json_filename)
read(yaml_filename)
read(xml_filename)