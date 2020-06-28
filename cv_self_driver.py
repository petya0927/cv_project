import cv2
import numpy
import utils

def getLaneCurve(img):

    imgCopy = img.copy()

    imgThres = utils.thresholding(img)

    h, w, c = img.shape
    points = utils.valTrackbars()
    imgWarp = utils.warpimg(imgThres, points, w, h)
    imgWarpPoints = utils.drawPoints(imgCopy, points)

    basePoints, imgHist = utils.getHistogram(imgWarp)

    cv2.imshow("Thres", imgThres)
    cv2.imshow("Warp", imgWarp)
    cv2.imshow("Warp Points", imgWarpPoints)
    cv2.imshow("Histogram", imgHist)
    return None

framecount = 0

if __name__ == "__main__":
    cap = cv2.VideoCapture("vid1.mp4")

    initalTrackBarVals = [102, 80, 20, 215]
    utils.initializeTrackbars(initalTrackBarVals)

    while True:

        framecount += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == framecount:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            framecount = 0

        success, img = cap.read()

        img = cv2.resize(img, (480, 240))

        getLaneCurve(img)

        cv2.imshow("Vid", img)
        cv2.waitKey(1)