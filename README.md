# League Vision Challenge

## Introduction

**Yolov4 artificial neural network, trained to detect and count champions health bars on the League of Legends game image files.**

The artificial neural network was trained with help of the Darknet framework, using Google Colaboratory.

In order to collect dataset, *jpg* images were extracted from gameplay videos with a frequency of 0.2 *fps*. Over 2100 images were collected.
Images extraction was realized, using `extract_frames.py` script.

Labels for the images were created manually, using LabelImg program. Example dataset is presented in the *example_dataset* folder.

## Run detection

To plot every image from given directory with bounding boxes and total score, run `run_yolo_detection.py` script and enter images directory.
To print total number of champions health bars in the image, run `run_yolo_count.py`.
Pass images names as a command line arguments e.g. `python run_yolo_count.py img1.jpg img2.jpg img3.jpg`
<p align="center"> 
<img src="doc/detected2.PNG">
</p>
