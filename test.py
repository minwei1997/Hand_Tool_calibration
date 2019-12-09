import numpy as np

A = np.zeros(shape=(1,3))
b=np.zeros(shape=(1,1))

t = np.array([3,3,3])
A=t
ans=np.vstack((A,t))

g = np.array([1])
b=g
a2 = np.vstack((b,g))

print(ans)
print(a2)