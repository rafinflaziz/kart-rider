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

def recognize():
    '''Take screenshot from some part of the screen,
    detect white-ish color from the picture, and return the recognized digit'''
    # grab screenshot from specific part (in pixel): vertical from 108 to 480, horizontal from 11 to 43
    pic = ImageGrab.grab(bbox = (11, 108, 43, 480))
    image = np.array(pic.getdata(), dtype = 'uint8').reshape((pic.size[1], pic.size[0], 3))

    # lower and upper bound for color range. In this case, white-ish color
    lower = np.array([130, 130, 130], dtype = "uint8")
    upper = np.array([255, 255, 255], dtype = "uint8")

    # mask the image, so it only shows white-ish color.
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)

    # recognize text from the masked image
    text = pytesseract.image_to_string(output, config="--psm 6")
    text = re.sub('[^A-Za-z0-9]+', ' ', text)

    # show the image
    cv2.imshow('masked', output)

    # to slow down the process.
    # because players' position changes slowly, we only need 1 record at ~1 second
    time.sleep(0.8)
    return text

def waiting():
    '''if the match ended, the program will wait until it started again'''
    digits = 0
    while digits < 2 or digits > 5:
        # if there are only few recognized digit, or too much recognized digit, we don't count that as a position standing.

        # so, we will repeat the process until there are reasonable amount of recognized digit (2 <= amount <= 5)
        text = recognize()
        digits = sum(map(str.isdigit, text)) # to count how many digits recognized

    return 0

while(1):

    #gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    #gray = cv2.erode(gray, np.array((7, 7)), iterations=1)
    #thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 2)
    #erode = cv2.erode(gray, None, iterations=1)

    # recognize text in the screen
    text = recognize()
    text = text.strip().split(' ')

    # if < 3 or > 5 text recognized, most likely the game has ended, so we will wait and pass the current process
    if len(text) < 3 or len(text) > 5:
        waiting()
        pass

    # list for result (size: 5)
    res = [None]*5
    res[:len(text)] = text
    print(res)
    result.append(res)

    # to quit the process, simply press q
    key = cv2.waitKey(25)
    if key == ord('q'):
        cv2.destroyAllWindows()
        break

# write the result to result.txt
file = open("result.txt", "w")
file.write(repr(result))
file.close()