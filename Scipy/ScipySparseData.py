# Create a CSR matrix from an array:
import numpy as np
from scipy.sparse import csr_matrix
arr=np.array([0,0,0,0,0,1,1,0,2])
print(csr_matrix(arr))
# sparse matrix methods
# viewing stored data (not the zero items)with the data property
import numpy as np
from scipy.sparse import csr_matrix
arr=np.array([[0,0,0],[0,0,1],[1,0,2]])
print(csr_matrix(arr).data)

# Counting nonzeros with the count_nonzero() method:
import numpy as np
from scipy.sparse import csr_matrix
arr=np.array([[0,0,0],[0,0,1],[1,0,2]])
print(csr_matrix(arr).count_nonzero())
# Removing zero-entries from the matrix with the eliminate_zeros() method:
import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
mat=csr_matrix(arr)
mat.eliminate_zeros()
print(mat)
# Eliminating duplicates by adding them:
import numpy as np
from scipy.sparse import csr_matrix
arr=np.array([[0,0,0],[0,0,1],[1,0,2]])
mat=csr_matrix(arr)
mat.sum_duplicates()
print(mat)
# Converting from csr to csc with the tocsc() method:
import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
newarr=csr_matrix(arr).tocsc()
print(newarr)