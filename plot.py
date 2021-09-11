# --------------------------------------------------------------------------------------------------------------------
#
#   Plotting script that plots 
#
# --------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt 
import numpy as np 
from math import floor

# Variables 
directory = "results/Omega_10_tau_02_phi_pi/"
photon_bin_cut_off = 40 
end_time = 100 
tau = 0.2
waiting_bar_count = 30 

# If plotting test files in direct directory set true 
local = True
if local == False:
    spin_down_file = "spin_down_total.txt"
    spin_up_file = "spin_up_total.txt"
    photon_counting_file = "photon_counting_total.txt"
    waiting_time_file = "waiting_time_total.txt"
    delimeter = ","
else:
    directory = "./"
    spin_down_file = "spin_down.txt"
    spin_up_file = "spin_up.txt"
    photon_counting_file = "photon_counting.txt"
    waiting_time_file = "waiting_time.txt"
    delimeter = None 

# Import data 
spin_down_data = np.loadtxt(directory + spin_down_file, delimiter=delimeter)
spin_up_data = np.loadtxt(directory + spin_up_file, delimiter=delimeter)
photon_data = np.loadtxt(directory + photon_counting_file)
waiting_data = np.loadtxt(directory + waiting_time_file, delimiter=delimeter)

### Spin up and down plots 
time_list = spin_down_data[:,0]
spin_down_data = spin_down_data[:,1]
spin_up_data = spin_up_data[:,1]

plt.figure(1)
plt.plot(time_list, spin_down_data, linewidth=0.5)
plt.grid()
plt.xlabel("Time (s)")
plt.ylabel("Ground state probability")
plt.xticks(np.arange(min(time_list), max(time_list)+1, 10.0))
plt.yticks(np.arange(np.floor(np.min(spin_down_data)), np.ceil(np.max(spin_down_data)), 0.25))

plt.figure(2)
plt.plot(time_list, spin_up_data, linewidth=3)
plt.grid()
plt.xlabel("Time (s)")
plt.ylabel("Excited state probability")

### Photon counting distribution plots 
x = [i for i in range(photon_bin_cut_off)]
plt.figure(3)
plt.bar(x, photon_data[0:photon_bin_cut_off])
plt.xlabel("Photon Number")
plt.ylabel("frequency")

### Waiting time distribution plots 
waiting_time = waiting_data[:,0]
waiting_data = waiting_data[:,1]
plt.figure(4)
plt.bar(waiting_time, waiting_data, width=0.2)
plt.xlabel("waiting time")
plt.ylabel("frequency")

# Take information before tau 
waiting_time_f = waiting_time[0:11]
waiting_data_f = waiting_time[0:11]

plt.figure(5)
plt.bar(waiting_time_f, waiting_data_f, width=0.01)
plt.xlabel("waiting time")
plt.ylabel("frequency")

# Take information after tau 
waiting_time_l = waiting_time[11:-1]
waiting_data_l = waiting_data[11:-1]

reduced_waiting_time_l = np.linspace(tau, end_time, waiting_bar_count)
reduced_waiting_data_l = np.zeros(waiting_bar_count)
increment = (end_time - tau) / waiting_bar_count

for i in range(len(waiting_time_l)):

    val = waiting_time_l[i] - tau 
    c = floor(val/increment)

    reduced_waiting_data_l[c] += waiting_data_l[i]

plt.figure(6)
plt.bar(reduced_waiting_time_l, reduced_waiting_data_l, width=0.1)
plt.xlabel("waiting time")
plt.ylabel("frequency")

# Show all plots 
plt.show()