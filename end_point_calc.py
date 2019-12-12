import numpy as np


R06 = np.array

def end_point_coor_of_tool(R06,X,Y,Z,tool_length):
    XYZ_06 = np.array([X,Y,Z,1]).reshape(4,1)
    
    T06 = np.vstack((R06,np.zeros(shape=(1,3))))
    T06 = np.hstack((T06,XYZ_06))
    tool_vector = np.array([0,0,tool_length,1]).reshape(4,1)
    end_coor_of_tool = T06.dot(tool_vector)

    return end_coor_of_tool
     


# test
if __name__ == "__main__":
    tool_length = 185
    R06 = np.array([[-0.85868905, 0.11627444, -0.49913261],
                    [-0.23955806, 0.76991136,  0.59147987],
                    [0.45306186,  0.62746852, -0.63325998]])
    X = 134.3662 
    Y = 286.2571 
    Z = 475.3393

    end_coor = end_point_coor_of_tool(R06,X,Y,Z,tool_length)
    print(np.transpose(end_coor))
    c = np.array(end_coor[:3])
    print(c[1])