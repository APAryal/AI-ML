# slice elements from index 1 to index 5 from the following array
import numpy as np
arr=np.array([1,2,3,4,5,6])
print(arr[1:5])
# slice elements from index 4 to the end of the array
import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr[4:])
# slice element from the beginning to index 4  not include
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
print(arr[:4])
# slice form the index 3 form the end index 1 for the end usi the minus operator to refer to an index from the end
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
print(arr[-3:-1])
# use the step value to determine the step of the slicing
# return every other element from index 1 to index 5 differnt 2
import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr[1:5:2])
# return every other element from the entire array
import numpy as np 
arr=np.array([1,2,3,4,5,6,7])
print(arr[::2])

# from the second element slice elements from index 1 to index 4 (not included )
import numpy as np 
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,1:4])

# from the both element return index 2
import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0:2,2])
# from both elements slice index 1 to index 4 (not included this will return a 2-d array)
import numpy as np 
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0:2, 1:4])