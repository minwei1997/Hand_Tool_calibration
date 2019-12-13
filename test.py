import numpy as np
from numpy.linalg import inv

T7_6 = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,190],[0,0,0,1]])
tool_coor = np.array([-66.6869,413.713,227.0881,1]).reshape(4,1)

ans = T7_6.dot(tool_coor)

print(ans)