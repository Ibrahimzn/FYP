import torch
import torchvision
import numpy as np
import cv2
import matplotlib
import math
from time import sleep
from PIL import ImageGrab
TIME_MULTIPLIER = 1.25



class ObjDetection:

    pos = [(200, 200, 1000, 700),#upper left
    (200, 900, 1000, 1350),#lower left
    (1500, 900, 2350, 1350),#lower right
    (1500, 200, 2350, 700)] #lower left
    
    def loadModel(self,conf):
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu') # here to tell the model to use GPU if available or CPU if not
        model = torch.hub.load('yolov7', 'custom', 'yolov7/runs/train/exp11/weights/last.pt', source='local',force_reload = True, verbose=False) # here to load the model
        model.conf = conf # here to set the confidence thresholds
        print('Model Confidence: ', model.conf, '\n') # here to print the confidence threshold to debug
        return model


    def detectObject(self,model,light):
        # Capture screenshot from each window or camera
        Img = np.array(ImageGrab.grab(bbox =(self.pos[light])))
        grayImg = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY) # here to convert the image to grayscale
        results = model(grayImg) # here to detect the objects
        #results.print()
        numOfCars = len(results.pandas().xyxy[0]) # here to get the number of cars detected
        seconds = self.calculateTime(numOfCars)
        return seconds, light
    
    
    def calculateTime(self, numOfCars):
        seconds = 0
        if numOfCars == 0:
            seconds = 0
        elif numOfCars > 0 and numOfCars <= 5:
            seconds = 7
        elif numOfCars > 5: 
            seconds = numOfCars * TIME_MULTIPLIER
            if seconds > 40: seconds = 40
        return math.ceil(seconds)