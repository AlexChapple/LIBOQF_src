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
directory = "results/Omega_10_tau_01_phi_0/"
photon_bin_cut_off = 25 
end_time = 100
tau = 0.2
waiting_bar_count = 25 

# If plotting test files in direct directory set true 
local = False
Large = False
if local == False:
    spin_down_file = "spin_down_total.txt"
    spin_up_file = "spin_up_total.txt"
    photon_counting_file = "photon_counting_total.txt"
    waiting_time_file = "waiting_time_total.txt"
    delimeter = ","
elif local == True and Large == False:
    directory = "./"
    spin_down_file = "spin_down_e.txt"
    spin_up_file = "spin_up_e.txt"
    photon_counting_file = "photon_counting_e.txt"
    waiting_time_file = "waiting_time_e.txt"
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
waiting_data = np.loadtxt(directory + waiting_time_file, delimiter=delimeter)

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

### Waiting time distribution plots 
waiting_time = waiting_data[:,0]
waiting_data = waiting_data[:,1]
fig4 = plt.figure(4)
fig4.set_size_inches(18.5, 10.5)
plt.bar(waiting_time, waiting_data, width=0.1, color=colours.french_violet)
plt.xlabel("waiting time")
plt.ylabel("frequency")
plt.title("Total waiting time distribution")
plt.savefig("waiting_time.pdf", dpi=600)

# Take information before tau 
waiting_time_f = waiting_time[0:20]
waiting_data_f = waiting_data[0:20]

fig5 = plt.figure(5)
fig5.set_size_inches(18.5, 10.5)
plt.bar(waiting_time_f, waiting_data_f, width=0.005)
plt.xlabel("waiting time")
plt.ylabel("frequency")
plt.title("waiting time distribution under $\\tau = 0.2$")
plt.savefig("waiting_time_before.pdf", dpi=600)

# Take information after tau 
waiting_time_l = waiting_time[21:-1]
waiting_data_l = waiting_data[21:-1]

reduced_waiting_time_l = np.linspace(tau, end_time, waiting_bar_count)
reduced_waiting_data_l = np.zeros(waiting_bar_count)
increment = (end_time - tau) / waiting_bar_count

for i in range(len(waiting_time_l)):

    val = waiting_time_l[i] - tau 
    c = floor(val/increment)

    reduced_waiting_data_l[c] += waiting_data_l[i]

fig6 = plt.figure(6)
fig6.set_size_inches(18.5, 10.5)
plt.bar(reduced_waiting_time_l, reduced_waiting_data_l, width=0.5)
plt.xlabel("waiting time")
plt.ylabel("frequency")
plt.title("waiting time distribution after tau")
plt.savefig("waiting_time_after1.pdf", dpi=600)

# Takes information after tau but doesn't bin them into smaller bins 
fig7 = plt.figure(7)
fig7.set_size_inches(18.5, 10.5)
plt.bar(waiting_time_l, waiting_data_l, width=0.15)
plt.xlabel("waiting time")
plt.ylabel("frequency")
plt.title("waiting time distribution after $\\tau = 0.2$")
plt.savefig("waiting_time_after2.pdf", dpi=600)

# Show all plots 


# EXPERIMENTNAL: prints total emission count 
total = 0 
for i in range(len(photon_data)):
    total += photon_data[i]*i

print("photon emission count = ", total)