# Iterate on the elements of the following 1-D array:
import numpy as np
arr=np.array([1,2,3])
for x in arr:
    print(x)

    # Iterate on the elements of the following 2-D array:
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])  
for x in arr:
 print(x)  

# Iterate on each scalar element of the 2-D array:
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
for x in arr:
 for y in x:
     print(y)

    #  Iterate on the elements of the following 3-D array:
import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr:
   print(x)

# iterate down to the scalars
import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr:
   for y in x:
      for z in y:
         print(z)
# iterate through the following 3-D array:
import numpy as np
arr=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
for x in np.nditer(arr):
   print(x)  
   