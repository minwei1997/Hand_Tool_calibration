import numpy as np
from numpy.linalg import inv

A=np.array([[22,0,0],[0,24,0],[0,0,26]])
b=np.array([[143.39],[167.5885],[221]])
ans = (inv(np.transpose(A).dot(A)).dot(np.transpose(A))).dot(b)
print(ans)
