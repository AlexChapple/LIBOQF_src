# --------------------------------------------------------------------------------------------------------------------
#
#   Plotting script that plots 
#
# --------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt 
import numpy as np 
from math import floor
import matplotlib

# Variables 
directory = "results/Omega_10_tau_01_phi_0/"
photon_bin_cut_off = 16 
end_time = 100
tau = 0.2
waiting_bar_count = 25 

# Color palette 
plat = "#F5F5F5"
vio = "#B947FF"
mauve = "#E2AFFF"
vivid_vio = "#A10AFF"
spanish_gray = "#666666"
mauve2 = "#cbb2fe"

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
    spin_down_file = "spin_down.txt"
    spin_up_file = "spin_up.txt"
    photon_counting_file = "photon_counting.txt"
    waiting_time_file = "waiting_time.txt"
    delimeter = None 
elif local == True and Large == True:
    directory = "./"
    spin_down_file = "spin_down_large.txt"
    spin_up_file = "spin_up_large.txt"
    photon_counting_file = "photon_counting_large.txt"
    waiting_time_file = "waiting_time_large.txt"
    delimeter = None 

# Import data 
# spin_down_data = np.loadtxt(directory + spin_down_file, delimiter=delimeter)
# spin_up_data = np.loadtxt(directory + spin_up_file, delimiter=delimeter)
photon_data = np.loadtxt(directory + photon_counting_file)
waiting_data = np.loadtxt(directory + waiting_time_file, delimiter=delimeter)

matplotlib.rcParams.update({'font.size': 18})

# ### Spin up and down plots 
# time_list = spin_down_data[:,0]
# spin_down_data = spin_down_data[:,1]
# spin_up_data = spin_up_data[:,1]

# plt.figure(1)
# plt.plot(time_list, spin_down_data, linewidth=3)
# plt.grid()
# plt.xlabel("Time (s)")
# plt.ylabel("Ground state probability")
# plt.xticks(np.arange(min(time_list), max(time_list)+1, 1.0))
# plt.yticks(np.arange(np.floor(np.min(spin_down_data)), np.ceil(np.max(spin_down_data)), 0.25))

# plt.figure(2)
# plt.plot(time_list, spin_up_data, linewidth=3)
# plt.grid()
# plt.xlabel("Time (s)")
# plt.ylabel("Excited state probability")

### Photon counting distribution plots 
x_odd = []
x_even = []
odd_peaks = []
even_peaks = []
for i in range(len(photon_data[0:photon_bin_cut_off])):

    if i % 2 == 0: # even 
        x_even.append(i)
        even_peaks.append(photon_data[i])
    else:
        x_odd.append(i)
        odd_peaks.append(photon_data[i])

fig3 = plt.figure(3)
fig3.set_size_inches(18.5, 10.5)
ax = plt.axes()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(vivid_vio)
ax.spines['bottom'].set_color(vivid_vio)
ax.tick_params(axis='x', colors=spanish_gray)
ax.tick_params(axis='y', colors=spanish_gray)
ax.xaxis.label.set_color(spanish_gray)
ax.yaxis.label.set_color(spanish_gray)
plt.bar(x_even, even_peaks, color=vio, label="even peaks")
plt.bar(x_odd, odd_peaks, color=mauve, label="odd peaks")
# ax.set_facecolor(plat)
fig3.set_alpha(0)
fig3.set_facecolor("none")
plt.xticks(np.arange(0, photon_bin_cut_off, 1))
plt.xlabel("Photon Number")
plt.ylabel("frequency")
plt.legend()
plt.savefig("pretty.pdf", facecolor=fig3.get_facecolor(), transparent=True, dpi=600)

### Waiting time distribution plots 
waiting_time = waiting_data[:,0]
waiting_data = waiting_data[:,1]
fig4 = plt.figure(4)
fig4.set_size_inches(18.5, 10.5)
ax2 = plt.axes()
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_color(vivid_vio)
ax2.spines['bottom'].set_color(vivid_vio)
ax2.tick_params(axis='x', colors=spanish_gray)
ax2.tick_params(axis='y', colors=spanish_gray)
ax2.xaxis.label.set_color(spanish_gray)
ax2.yaxis.label.set_color(spanish_gray)
plt.bar(waiting_time[0:20], waiting_data[0:20], width=0.4, color=vio, label="waiting time within round trip time")
plt.bar(waiting_time[21:-1], waiting_data[21:-1], width=0.4, color=mauve2, label="waiting time after round trip time")
plt.xlabel("waiting time")
plt.ylabel("frequency")
plt.legend()
plt.title("Total waiting time distribution")
plt.savefig("pretty2.pdf", facecolor=fig3.get_facecolor(), transparent=True, dpi=600)


# # Take information before tau 
# waiting_time_f = waiting_time[0:20]
# waiting_data_f = waiting_data[0:20]

# plt.figure(5)
# plt.bar(waiting_time_f, waiting_data_f, width=0.005)
# plt.xlabel("waiting time")
# plt.ylabel("frequency")
# plt.title("waiting time distribution under $\\tau = 0.2$")

# # Take information after tau 
# waiting_time_l = waiting_time[21:-1]
# waiting_data_l = waiting_data[21:-1]

# reduced_waiting_time_l = np.linspace(tau, end_time, waiting_bar_count)
# reduced_waiting_data_l = np.zeros(waiting_bar_count)
# increment = (end_time - tau) / waiting_bar_count

# for i in range(len(waiting_time_l)):

#     val = waiting_time_l[i] - tau 
#     c = floor(val/increment)

#     reduced_waiting_data_l[c] += waiting_data_l[i]

# plt.figure(6)
# plt.bar(reduced_waiting_time_l, reduced_waiting_data_l, width=0.5)
# plt.xlabel("waiting time")
# plt.ylabel("frequency")
# plt.title("waiting time distribution after tau")

# # Takes information after tau but doesn't bin them into smaller bins 
# plt.figure(7)
# plt.bar(waiting_time_l, waiting_data_l, width=0.15)
# plt.xlabel("waiting time")
# plt.ylabel("frequency")
# plt.title("waiting time distribution after $\\tau = 0.2$")

# Show all plots 
plt.show()