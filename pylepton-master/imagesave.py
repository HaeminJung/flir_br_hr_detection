import numpy as np
import cv2
from pylepton import Lepton


with Lepton() as l:
    a,_ = l.capture()
print(np.shape(a))
cv2.normalize(a,a,0,65535,cv2.NORM_MINMAX)
np.right_shift(a,8,a)
print(a[20][20]/float(255))
cv2.imshow("Vid",a/float(255))
cv2.waitKey(0)
cv2.destroyAllWindows()
