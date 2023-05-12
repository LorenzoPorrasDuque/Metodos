import matplotlib.pyplot as plt
import scipy.stats
import csv
import numpy as np

""" mu = 5
scipy.stats.poisson.rvs(mu,size=1000) 
 """
data = []


with open("customers_per_day.csv") as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        data.append(float(row[0]))


dist = scipy.stats.poisson
bounds = [(-100, 100)]
res = scipy.stats.fit(dist, data, bounds)
print(res)
res.plot()
plt.show()
