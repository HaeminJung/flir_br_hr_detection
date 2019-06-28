import cv2
import numpy as np
#from pylepton import Lepton

frame = np.zeros((80,60))
frame +=1
cv2.imshow("Vid",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
