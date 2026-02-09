# logistic distribution is used to describe growth
# Used extensively in machine learning in logistic regression , neural networks etc
# it has three parameters:
# loc-mean, where the peak is default 0.
# scale-standard deviation , the flatness of distribution , default 1.
# size- The shape of the returned array


# Draw 2*3 samples from a logistic distribuion with mean at 1 and stddev 2.0
from numpy import random
x=random.logistic(loc=1, scale=2, size=(2,3))
print(x)

# Visualization of logistic distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.logistic(size=1000), kind="kde")
plt.show()

# Difference between logistic and normal distribution
from numpy import random
import matplotlib.pyplot as plt 
import seaborn as sns
data={
    "normal":random.normal(scale=2, size=1000),
    "logistic":random.logistic( size=1000)
}
sns.displot(data, kind="kde")
plt.show()