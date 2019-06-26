from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
import time

##set the camera to cap
cap = cv2.VideoCapture(0)
if cap.isOpened() == False: #Check for Camera
    print ('Can\'t open the CAM(%d)' % (CAM_ID))
    exit()

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)

prevTime = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    resize = cv2.resize(frame, (480, 320)) 
    resize = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # detect faces in the grayscale image
    rects = detector(resize, 0)
    
    # loop over the face detections
    for (i, rect) in enumerate(rects):
        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy
        # array
        shape = predictor(resize, rect) #shape holds the (x,y) coordinate of facial regions
        shape = face_utils.shape_to_np(shape) #returns a np.array of (x,y) coordinates



        # loop over the (x, y)-coordinates for the facial landmarks
        # and draw them on the image
        for (x, y) in shape:
            cv2.circle(resize , (x, y), 2, (144, 144, 0), -1)

    #Mirror Image
    mirroredImage = cv2.flip(resize,1)

    #Calculate framerate
    incomingTime = time.time()

    timePerFrame = incomingTime - prevTime
    prevTime = incomingTime

    #Find FPS by diving one
    fps = 1/(timePerFrame)

    # Print to console
    #print "Time {0} " . format(timePerFrame)
    # print "Estimated fps {0} " . format(fps)

    # Store FPS inst string
    fps_string = "FPS : %0.1f" % fps

    # Write on Frame
    cv2.putText(mirroredImage, fps_string, (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (10, 10, 10), 2)

    # Display the resulting frame
    cv2.imshow('frame', mirroredImage)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


