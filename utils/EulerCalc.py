import numpy as np

# define a function for calculate Euler Angle
def EulerAngle2Rot(A,B,C):
    R_z = np.array([[np.cos(C*np.pi/180), -np.sin(C*np.pi/180), 0],
                    [np.sin(C*np.pi/180),  np.cos(C*np.pi/180), 0],
                    [0,                    0,                   1]])

    R_y = np.array([[ np.cos(B*np.pi/180),    0,    np.sin(B*np.pi/180)],
                    [ 0,                      1,    0                  ],
                    [-np.sin(B*np.pi/180),    0,    np.cos(B*np.pi/180)]])

    R_x = np.array([[1,     0,                       0                  ],
                    [0,     np.cos(A*np.pi/180),    -np.sin(A*np.pi/180)],
                    [0,     np.sin(A*np.pi/180),     np.cos(A*np.pi/180)]])

    # R06 = R_z*R_y*R_x
    R06 = R_z.dot(R_y.dot(R_x))

    return R06

# test
if __name__ == "__main__":
    A = 135.2632
    B = -26.9403
    C = -164.4119
    R06 = EulerAngle2Rot(A,B,C)
    print(R06)