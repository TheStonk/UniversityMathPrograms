import numpy as np

a = np.array([[1,2],
              [3,4],
              [5,6]])
b = np.array([[1,2,3],
              [1,2,3]])
c = a@b
d = b@a
print(c@d) # multiply two matrix, use @ for matrix mul
#print(b.transpose()) # Transpose matrix
#print(a+a)
