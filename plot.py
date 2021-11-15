# --------------------------------------------------------------------------------------------------------------------
#
#   Plotting script that plots 
#
# --------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt 
import numpy as np 
from math import floor
import matplotlib
import colours

# Variables 
directory = "results/Omega_10_tau_02_phi_pi/"
photon_bin_cut_off = 25 
end_time = 100
tau = 0.2
waiting_bar_count = 25 

# If plotting test files in direct directory set true 
local = True
Large = False
if local == False:
    spin_down_file = "spin_down_total.txt"
    spin_up_file = "spin_up_total.txt"
    photon_counting_file = "photon_counting_total.txt"
    waiting_time_file = "waiting_time_total.txt"
    delimeter = ","
elif local == True and Large == False:
    directory = "./"
    spin_down_file = "spin_down.txt"
    spin_up_file = "spin_up.txt"
    photon_counting_file = "photon_counting.txt"
    delimeter = None 
elif local == True and Large == True:
    directory = "./"
    spin_down_file = "spin_down_large.txt"
    spin_up_file = "spin_up_large.txt"
    photon_counting_file = "photon_counting_large.txt"
    waiting_time_file = "waiting_time_large.txt"
    delimeter = None 

# Import data 
spin_down_data = np.loadtxt(directory + spin_down_file, delimiter=delimeter)
spin_up_data = np.loadtxt(directory + spin_up_file, delimiter=delimeter)
photon_data = np.loadtxt(directory + photon_counting_file)

matplotlib.rcParams.update({'font.size': 22})

### Spin up and down plots 
time_list = spin_down_data[:,0]
spin_down_data = spin_down_data[:,1]
spin_up_data = spin_up_data[:,1]

fig1 = plt.figure(1)
fig1.set_size_inches(18.5, 10.5)
plt.plot(time_list, spin_down_data, linewidth=0.5)
plt.grid()
plt.xlabel("Time (s)")
plt.ylabel("Ground state probability")
plt.xticks(np.arange(min(time_list), max(time_list)+1, 10.0))
plt.yticks(np.arange(np.floor(np.min(spin_down_data)), np.ceil(np.max(spin_down_data)), 0.25))
plt.savefig("ground_state.pdf", dpi=600)

fig2 = plt.figure(2)
fig2.set_size_inches(18.5, 10.5)
plt.plot(time_list, spin_up_data, linewidth=3)
plt.grid()
plt.xlabel("Time (s)")
plt.ylabel("Excited state probability")
plt.savefig("excited_state.pdf", dpi=600)

### Photon counting distribution plots 
x = [i for i in range(photon_bin_cut_off)]
fig3 = plt.figure(3)
fig3.set_size_inches(18.5, 10.5)
plt.bar(x, photon_data[0:photon_bin_cut_off])
plt.xticks(np.arange(0, photon_bin_cut_off, 1))
plt.xlabel("Photon Number")
plt.ylabel("frequency")
plt.savefig("photon_counting.pdf", dpi=600)
