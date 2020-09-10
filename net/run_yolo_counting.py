import numpy as np
import cv2 as cv
import sys
import os


def detect():

    img_paths = ['screen1.png']	# default name

    if len(sys.argv) >= 2:
        img_paths = []
        for arg in sys.argv[1:]:
            img_paths.append(arg)
    
    cwd = os.getcwd()
    
    for img_path in img_paths:
        net_path = os.path.join(cwd, "yolov4/yolov4-obj_last.weights")
        cfg_path = os.path.join(cwd, "yolov4/yolov4-obj.cfg")

        if not os.path.exists(net_path):
            net_path = os.path.join(cwd, "yolov4/backups/yolov4-obj_last.weights")

        net = cv.dnn.readNet(net_path, cfg_path)

        layers = net.getLayerNames()
        output_layers = []
        for i in net.getUnconnectedOutLayers():
            output_layers.append(layers[i[0] - 1])

        img = cv.imread(img_path, 1)
        blob_img = cv.dnn.blobFromImage(img, np.round(1 / 255, 6), (416, 416), swapRB=True, crop=False)
        net.setInput(blob_img)
        outputs = net.forward(output_layers)

        confidences = []
        boxes = []

        for output in outputs:
            for detected in output:
                confidence = detected[5]

                if confidence > 0.3:
                    height, width, channels = img.shape
                    center_x = int(detected[0] * width)
                    center_y = int(detected[1] * height)
                    w = int(detected[2] * width)
                    h = int(detected[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    confidences.append(float(confidence))
                    boxes.append([x, y, w, h])

        indexes = cv.dnn.NMSBoxes(boxes, confidences, 0.5, 0.5)

        print(len(indexes))


try:
    detect()
except Exception as e:
    print(f"ERROR: {e}")

