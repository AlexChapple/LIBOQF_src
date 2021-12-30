"""
Plot g2 
"""

import numpy as np 
import matplotlib.pyplot as plt 

data = np.loadtxt("results_g2/g2.txt")
data2 = np.loadtxt("results_g2/avg_e.txt")[:,1]

norm = sum(data2) / np.size(data2)

time_list = data[:,0]
G2_list = data[:,1]

g2_list = G2_list / norm**2 

plt.plot(time_list, g2_list)
plt.show()