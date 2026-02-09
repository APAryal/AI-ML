# Generate a random 1*10 distribution for occurrence 2
from numpy import random
x=random.poisson(lam=2, size=10)
print(x)

#visualization of poisson distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.poisson(lam=2, size=1000))
plt.show() 
# different Between Normal and poisson distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
data={
    "normal":random.normal(loc=50, scale=7, size=1000),
    "poisson":random.poisson(lam=50, size=1000)
}
sns.displot(data ,kind="kde")
plt.show()
# Difference between binomial and poisson distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
data={
    "binomial":random.binomial(n=1000, p=0.01, size=1000),
    "poisson":random.poisson(lam=10, size=1000)
}
sns.displot(data, kind="kde")
plt.show()