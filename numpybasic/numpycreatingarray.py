# create a numpy ndarray object using the array()function
import numpy as np
arr=np.array([1,4,6,8])
print(arr)
print(type(arr))
# output[1 4 6 8]
# <class 'numpy.ndarray'>

# Use a tuple to create a NumPy array:
import numpy as np
arr =np.array ((1, 2, 5,7, 9,))
print(arr)
# Dimensions in Arrays
# 0-D Arrays
import numpy as np
arr=np.array(67)
print(arr)
# 1-D array
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)

# 2-D array
import numpy as np
arr=np.array([[1,2,3,7],[4,5,6,8]])
print(arr)
# Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:
import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr)

# check the how many dimension in arrays
import numpy as np
a=np.array(23)
b=np.array([1,2,3])
c=np.array([[1,2,3,4],[5,6,7,7]])
d=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[5,6,7]]])
print(a)
print(a.ndim)
print(b)
print(b.ndim)
print(c)
print(c.ndim)
print(d, d.ndim )
# Higher dimension array
import numpy as np
arr=np.array([1,2,3],ndmin=7)
print(arr)
print(arr.ndim)
