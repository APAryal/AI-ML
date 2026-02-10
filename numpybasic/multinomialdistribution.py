# multinomial distribution is a generalization of binomial distribution
# It describe outcomes of multi-nomial senarios unlike binomial where scenarios must be only one of two e.g. Blood type of population, dice roll outcome.
# It has three parameters:
# n-number of times to run the experiment
# pvals-list of probabilities os outcomes(e.g.[1/6, 1/6, 1/6, 1/6, 1/6, 1/6]for dice roll)
# size- The shape of the returned array.

# Draw out a smaple for dice roll:
from numpy import random
x=random.multinomial(n=6, pvals=[1/6,1/6,1/6,1/6,1/6,1/6])
print(x)

