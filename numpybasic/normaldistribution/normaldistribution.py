# Generate a random normal distribution of size 2*3
from numpy import random
x=random.normal(size=(2,3))
print(x)
# Generate a random normal distribution of size 2*3 with mean at 1 and standard deviation of 2:
from numpy import random
x=random.normal(loc=1, scale=2, size=(2,3))
print(x)
# visualization of noraml distribuation
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.normal(size=1000),kind="kde")
plt.show()