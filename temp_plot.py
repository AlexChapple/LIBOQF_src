import numpy as np 
import matplotlib.pyplot as plt 

# Load data 
spin_down_data = np.loadtxt("results/spin_down.txt")
photon_data = np.loadtxt("results/photon_counting.txt")

# Plot spin 
plt.figure(1)
time_list = spin_down_data[:,0]
spin_down_list = spin_down_data[:,1]
plt.plot(time_list, spin_down_list)

# Plot photon count 
plt.figure(2)
photon_range = 80 
plt.bar(range(0,photon_range), photon_data[0:photon_range])


plt.show()