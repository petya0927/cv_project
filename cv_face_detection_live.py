import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 500)

faceCascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(grayFrame, 1.1, 4)

    objectType = "face"
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, objectType, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)
        
    cv2.imshow("Video", frame)
    
    if cv2.waitKey(1) == 27:
        break
