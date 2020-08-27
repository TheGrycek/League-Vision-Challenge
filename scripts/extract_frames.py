import numpy as np
import cv2 as cv
import os

'''
Script extracts frames from video files with given frequency
'''

def extract_frames():
    print("Enter video directory:")
    path = input()
    print("Enter the number of frames per second:")
    f = float(input())

    os.makedirs("images", exist_ok=True)
    images_dir = os.path.join(os.getcwd(), "images")
    cap = cv.VideoCapture(path)
    success = True
    num = 1
    img_num = 1

    while success:
        cap.set(cv.CAP_PROP_POS_MSEC, (num * (1000/f)))
        success, img = cap.read()
        last = cv.imread("frame{}.jpg".format(num - 1))

        if np.array_equal(img, last):
            break

        image_name = "image%d.jpg" % img_num
        image_dir = os.path.join(images_dir, image_name)

        while os.path.exists(image_dir):
            print(f"DIRECTORY {image_dir} EXISTS")
            img_num += 1
            image_name = "image%d.jpg" % img_num
            image_dir = os.path.join(images_dir, image_name)

        cv.imwrite(image_dir, img)
        print(image_name)
        num += 1
        img_num += 1


try:
    extract_frames()

except Exception as e:
    print(e)
    extract_frames()
