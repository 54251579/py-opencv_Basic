import numpy as np
import cv2 as cv

json_filename = 'img/save_img/data.json'
yaml_filename = 'img/save_img/data.yml'
xml_filename = 'img/save_img/data.xml'

def write(filename):
    name = 'Jane'
    age = 10
    pt1 = (100, 50)
    scoures =(80,90,70)
    mat1 = np.array([[1.0, 1.5], [2.0, 3.1]], dtype=np.float64)
    fs = cv.FileStorage(filename, cv.FILE_STORAGE_WRITE)

    if not fs.isOpened():
        print('file open failed')
        return
    
    fs.write('name', name)
    fs.write('age', age)
    fs.write('point', pt1)
    fs.write('scoures', scoures)
    fs.write('data', mat1)

    fs.release()

write(json_filename)
write(yaml_filename)
write(xml_filename)