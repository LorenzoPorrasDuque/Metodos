from scipy.stats import expon, kstest
import matplotlib.pyplot as plt
import scipy.stats
import csv
import numpy as np

data = scipy.stats.poisson.rvs(7, size=25)
dist = scipy.stats.poisson
bounds = [(-100, 100)]
res = scipy.stats.fit(dist, data, bounds)
print(res)
kstest_result = scipy.stats.kstest(data, 'poisson', args=[res.params[0]])
print("KS test p-value:", kstest_result[1])
res.plot()
plt.show()
