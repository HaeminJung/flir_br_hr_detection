import numpy as np
import cv2
from pylepton import Lepton

def getIm():
    with Lepton() as l:
        a,_ = l.capture()
    cv2.normalize(a,a,0,65535,cv2.NORM_MINMAX)
    np.right_shift(a,8,a)

    cv2.imshow("a",a)

    return a/float(255)
