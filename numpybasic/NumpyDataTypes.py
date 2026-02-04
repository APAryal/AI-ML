# Get the data type of an array object
import numpy as np
arr=np.array([1,2,3,4,5,6,6])
print(arr.dtype)
# get the data type of an array constaining string
import numpy as np
arr=np.array(["apple", "babana","cherry"])
print(arr.dtype)
# create an array with data type string
import numpy as np 
arr=np.array([1,2,3,4,5], dtype='S')
print(arr)
print(arr.dtype)
# create an array with data type 4 bytes interger
import numpy as np
arr=np.array([1,2,3,4], dtype='i4')
print(arr)
print(arr.dtype)
# # A non interge string 'a can not be converted to interger (will raise an error)
# import numpy as no
# arr= np.array(['a', '2,'], dtype='i')
# print(arr.dtype)

# change dat type from to interger by using 'i as parameter value
import numpy as np 
arr=np.array([1.1, 2.1, 5.6])
newarr=arr.astype('i')
print(newarr)
print(newarr.dtype)
# change the data type fload to integer by using int as parameter value:
import numpy as np
arr=np.array([1.2,4.5,6.7])
newarr=arr.astype(int)
print(newarr)
print(newarr.dtype)
# change data type from interger to boolean
import numpy as np
arr=np.array([1,0,9,7])
newarr=arr.astype(bool)
print(newarr)
print(newarr.dtype)