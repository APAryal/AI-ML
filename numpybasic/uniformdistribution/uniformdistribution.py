# used to describe probability where every event has equal chances of occuring EG generation of random numbers
# low-lower bound-default 0.0
# high- upper bound -default 1.0
# size- The shape of the returned array
# Create a 2*3 uniform distribution sample
from numpy import random
x=random.uniform(size=(2,3))
print(x)
# Visualization of Uniform Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.uniform(size=100), kind="kde")
plt.show()