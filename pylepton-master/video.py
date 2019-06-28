import cv2
import image
import numpy as np

while(True):
    frame = image.getIm()
#    print(frame)
    resize = cv2.resize(frame,(160,120))
    cv2.imshow("Vid",resize)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cv2.waitKey(0)
cv2.destroyAllWindows()

