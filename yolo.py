import cv2
import numpy as np

cap = cv2.VideoCapture(0)

whT = 320

classesFile = "coco.names"
classNames = []

f = open(classesFile, "rt")

classNames = f.read().rstrip("\n").split("\n")

f.close()

modelConfig = 'yolov3.cfg'
modelWeights = 'yolov3.weights'

net = cv2.dnn.readNetFromDarknet(modelConfig, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

while True:
    success, img = cap.read()
    
    blob = cv2.dnn.blobFromImage(img, 1/255, (whT, whT), [0, 0, 0], 1, crop=False)
    net.setInput(blob)

    layerNames = net.getLayerNames()
    #print (layerNames)
    
    outputNames = [layerNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    #print (outputNames)
    #print (net.getUnconnectedOutLayers())
    
    outputs = net.forward(outputNames)
    
    print (outputs[0].shape)
    print (outputs[1].shape)
    print (outputs[2].shape)
    
    cv2.imshow('Image', img)
    cv2.waitKey(1)



















