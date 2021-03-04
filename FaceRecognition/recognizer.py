
import cv2
import numpy as np
import os
import sys

def mostFrequent(arr, n):
    
        # Sort the array
        arr.sort()

        # find the max frequency using
        # linear traversal
        max_count = 1; res = arr[0]; curr_count = 1

        for i in range(1, n):
            if (arr[i] == arr[i - 1]):
                curr_count += 1

            else :
                if (curr_count > max_count):
                    max_count = curr_count
                    res = arr[i - 1]

                curr_count = 1

        # If last element is most frequent
        if (curr_count > max_count):

            max_count = curr_count
            res = arr[n - 1]

        return res
def recognizer():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);

    font = cv2.FONT_HERSHEY_SIMPLEX

    #iniciate id counter
    id = ''
    face = []

    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    while True:

        ret, img =cam.read()
        # img = cv2.flip(img, -1) # Flip vertically

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
        )

        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

            # Check if confidence is less them 100 ==> "0" is perfect match 
            if (confidence < 100):
                # print(StudentNumbers[id])

                if confidence<50:
                    print("Face captured"+ str(len(face)))
                    face.append(id)
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
            
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
        
        cv2.imshow('camera',img) 

        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        count = len(face)
        if count>15:
            break
    stuId = mostFrequent(face,count)
    
    return(numberCorrector(stuId))
    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()
    sys.exit()

def numberCorrector(number):
    number = "b"+str(number)
    # print(number)
    o = 0
    original = ""
    original2 = ""
    while o<5:
        original = original + number[o]
        o=o+1
    # print(original)
    p=5
    while p<11:
        original2 = original2 + number[p]
        p=p+1
    # print(original2)
    now = original+"."+original2
    return(now)
