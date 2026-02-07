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
# 