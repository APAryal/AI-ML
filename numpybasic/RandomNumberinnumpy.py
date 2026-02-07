# Generate a random integer from 0 to 100:
from numpy import random
x=random.randint(100)
print(x)

# Generate a random float from 0 to 1:
from numpy import random
x=random.rand()
print(x)
# Generate a 1-d array containing 5 random intergers from 0 to 100
from numpy import random
x=random.randint(100, size=(5))
print(x)
# Generate a 2-D array with 3 rows each rew containing 5 random integers from 1 to 100
from numpy import random
x=random.randint(100, size=(3,5))
print(x)
# Generate a 1-D array containing 5 random floats
from numpy import random
x=random.rand(5)
print(x)
# Generate a 2_d array with 3 rows each row containing 5 random numbers
from numpy import random
x= random.rand(3,5)
print(x)
# Return one of the values in array:
from numpy import random
x=random.choice([3,5,7,9])
print(x)
# generate a 2-D array that consists of the valuse in the array parameter (3,5,7, and 9):
from numpy import random
x=random.choice([3,5,7,9],size=(3,5))
print(x)