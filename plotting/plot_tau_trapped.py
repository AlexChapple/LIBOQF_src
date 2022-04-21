# Plots the data for tau 0.4, 0.6, 0.8 

import matplotlib.pyplot as plt 
import numpy as np 

# Parameters 
duration = 20 

# Import data 
tau_list = [0.4, 0.6, 0.8]
time_steps = [10000, 8000]

spin_up_list = []
spin_down_list = []
photon_list = []

for tau in tau_list:

    spin_up_data = np.load("results/tau04/spin_up_total.npy")
    spin_down_data = np.load("results/tau04/spin_down_total.npy")
    photon_data = np.load("results/tau04/photon_counting_total.npy")

    spin_up_list.append(spin_up_data)
    spin_down_list.append(spin_down_data)
    photon_list.append(photon_data)

### ----- Plotting ------------------------------------

# Spin up 



