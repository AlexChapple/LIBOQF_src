import numpy as np 
import matplotlib.pyplot as plt 

# Load data 
spin_down_data = np.loadtxt("results/spin_down.txt")

time_list = spin_down_data[:,0]
spin_down_list = spin_down_data[:,1]

plt.plot(time_list, spin_down_list)
plt.show()