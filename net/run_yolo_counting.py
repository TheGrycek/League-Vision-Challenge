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

    for img_path in img_paths:
        net_path = os.path.join(os.getcwd(), "yolov4/yolov4-obj_last.weights")
        cfg_path = os.path.join(os.getcwd(), "yolov4/yolov4-obj.cfg")

        if not os.path.exists(net_path):
            net_path = os.path.join(os.getcwd(), "yolov4/backups/yolov4-obj_last.weights")

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
        class_nums = []
        boxes = []

        for output in outputs:
            for detected in output:
                scores = detected[5:]
                class_num = np.argmax(scores)
                confidence = scores[class_num]

                if confidence > 0.3:
                    center_x = int(detected[0] * img.shape[1])
                    center_y = int(detected[1] * img.shape[0])
                    w = int(detected[2] * img.shape[1])
                    h = int(detected[3] * img.shape[0])
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    confidences.append(float(confidence))
                    class_nums.append(class_num)
                    boxes.append([x, y, w, h])

        indexes = cv.dnn.NMSBoxes(boxes, confidences, 0.5, 0.5)

        bars_amount = len(indexes)
        if bars_amount > 10:
            bars_amount = 10

        print(bars_amount)


try:
    detect()
except Exception as e:
    print(f"ERROR: {e}")

