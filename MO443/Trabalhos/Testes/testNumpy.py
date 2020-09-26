import cv2
import numpy as np


vis = np.zeros((384, 836), np.float32)
vis2 = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)

cv2.imshow('image', vis2)
cv2.waitKey(0)
cv2.destroyAllWindows()