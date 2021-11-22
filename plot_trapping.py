"""
Plots the results to show photon trapping

"""

import numpy as np 
import matplotlib.pyplot as plt 

directory = "results_trapping_test/"

data = np.loadtxt(directory + "spin_down.txt")

time_list = data[:,0]
ground_state_data = data[:,1]

plt.plot(time_list, ground_state_data, lw=0.1)

plt.show()