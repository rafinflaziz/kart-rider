import cv2
import pytesseract
import re
import time
import numpy as np
import pandas as pd
from PIL import ImageGrab   

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#image = cv2.imread("tes2.jpg")
# image = cv2.imread('testing.png')
result = []

def screen_shot():
    pic = ImageGrab.grab(bbox = (11, 108, 43, 480))
    image = np.array(pic.getdata(), dtype = 'uint8').reshape((pic.size[1], pic.size[0], 3))
    lower = np.array([130, 130, 130], dtype = "uint8")
    upper = np.array([255, 255, 255], dtype = "uint8")
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)
    text = pytesseract.image_to_string(output, config="--psm 6")
    text = re.sub('[^A-Za-z0-9]+', ' ', text)
    cv2.imshow('thresh', output)
    time.sleep(0.7)
    return text

def waiting():
    numbers = 0
    while numbers < 2 or numbers > 5:
        text = screen_shot()
        numbers = sum(map(str.isdigit, text))
    return 0

while(1):

    #gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    #gray = cv2.erode(gray, np.array((7, 7)), iterations=1)
    #thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 2)
    #erode = cv2.erode(gray, None, iterations=1)
    text = screen_shot()
    text = text.strip().split(' ')
    if len(text) < 3 or len(text) > 5:
        waiting()
        pass
    res = [None]*5
    res[:len(text)] = text
    print(res)
    result.append(res)
    key = cv2.waitKey(25)
    if key == ord('q'):
        cv2.destroyAllWindows()
        break

file = open("result.txt", "w")
file.write(repr(result))
file.close()