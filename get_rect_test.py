import cv2
import numpy as np
import dlib
from imutils import face_utils
import argparse
import imutils



cap = cv2.VideoCapture(0)
if cap.isOpened() == False: #카메라 생성 확인
    print ('Can\'t open the CAM(%d)' % (CAM_ID))
    exit()

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)

ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

rects = detector(gray,0)

for (i, rect) in enumerate(rects):
        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy
        # array
        shape = predictor(gray, rect) #shape holds the (x,y) coordinate of facial regions
        shape = face_utils.shape_to_np(shape) #returns a np.array of (x,y) coordinates

        print(shape)
        print(np.shape(shape))


print(np.shape(gray))
print(np.shape(frame))
print(ret)  

cap.release()
