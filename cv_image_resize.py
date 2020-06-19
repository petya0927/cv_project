import cv2
import numpy as np

img = cv2.imread("lena.png")
print (img.shape)

imResize = cv2.resize(img, (300, 300))
print (imResize.shape)

imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)
