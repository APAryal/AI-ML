# print the shape of a 2-D array
import numpy as np
arr=np.array([[1,2,3,4],[6,7,8,9]])
print(arr.shape)
# create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4
import numpy as np
arr=np.array([1,2,3,4],ndmin=5)
print(arr)
print('shape of array',arr.shape)


# reshape array in numpy
# convert the following 1-d array  12 elements into a 2-d array. The outermost dimenion will have 4 arrays , each with 3 elements
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(4,3)
print(newarr)
# convert the following 1-d array with 12 elements into a 3-d array the outermost dimension wil have 2 array that contains 3 arrays each with 2 elements
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(2,3,2)
print(newarr)

# check if the returned array is copy or a view
import numpy as np 
arr=np.array([1,2,3,4,5,6,7,8])
print(arr.reshape(2,4).base)

# convert 1d array with 8 elements to 3d array with 2*2 elements
import numpy as np 
arr=np.array([1,2,3,4,5,6,7,8])
newarr=arr.reshape(2,2,-1)
print(newarr)
# convert the array inot a 1d array
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
newarr=arr.reshape(-1)
print(newarr)