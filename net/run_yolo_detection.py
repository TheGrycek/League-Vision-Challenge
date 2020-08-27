import cv2 as cv
import numpy as np
import os

net_path = os.path.join(os.getcwd(), "yolov4/yolov4-obj_last.weights")
cfg_path = os.path.join(os.getcwd(), "yolov4/yolov4-obj.cfg")

if not os.path.exists(net_path):
    net_path = os.path.join(os.getcwd(), "yolov4/backups/yolov4-obj_last.weights")

net = cv.dnn.readNet(net_path, cfg_path)

print("Enter images path: ")
images_path = input()
img_names = os.listdir(images_path)

layers = net.getLayerNames()
output_layers = []
for i in net.getUnconnectedOutLayers():
    output_layers.append(layers[i[0] - 1])

extension = ".jpg"
class_name = "bar"
color = (0, 0, 255)
font_type = cv.QT_CHECKBOX

try:
    for img_name in img_names:
        if img_name.endswith(extension):

            img = cv.imread(os.path.join(images_path, img_name), 1)

            blob_img = cv.dnn.blobFromImage(img, np.round(1/255, 6), (416, 416), swapRB=True, crop=False)
            net.setInput(blob_img)
            outputs = net.forward(output_layers)

            class_nums = []
            confidences = []
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

            for i in range(len(boxes)):
                if i in indexes:
                    x, y, w, h = boxes[i]
                    img = cv.copyMakeBorder(img, 0, 60, 0, 60, cv.BORDER_CONSTANT, value=[0, 0, 0])
                    text = class_name + ":" + str(np.round(confidences[i], 3))
                    cv.putText(img, text, (x, y + 50), font_type, 2, color, 2)
                    cv.rectangle(img, (x, y), (x + w, y + h), color, 2)

            score = "score:" + str(len(indexes))
            cv.putText(img, score, (40, 40), font_type, 4, color, 3)
            img = cv.resize(img, None, fx=0.4, fy=0.4)
            cv.imshow("Processed image", img)
            cv.waitKey(0)

    cv.destroyAllWindows()

except Exception as e:
    print(e)
