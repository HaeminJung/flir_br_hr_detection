import cv2
import getThermal
import numpy as np

while(True):
    frame = getThermal.getIm()
#    print(frame)
    resize = cv2.resize(frame,(320,240))
    mirroredImage = cv2.flip(resize,1)
    cv2.imshow("Vid",mirroredImage)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cv2.destroyAllWindows()

