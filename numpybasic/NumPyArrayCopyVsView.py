# make a copy ,change the orginal array and display both array
import numpy as np
arr=np.array([1,2,3,4,5])
x=arr.copy()
arr[0]=42
print(arr)
print(x)
# make a view change the original array and display both arrays
import numpy as np
arr=np.array([1,2,3,4,5])
x=arr.view()
arr[0]=42
print(arr)
print(x)
# make a view , change the view and display both arrays
import numpy as np
arr=np.array([1,2,3,4,5])
x=arr.view()
x[0]=31
print(arr)
print(x)
# print the value of the base attribute to check if an array owns it's data or not
import numpy as np 
arr=np.array([1,2,3,4,5])
x=arr.copy()
y=arr.view()
print(x.base)
print(y.base)