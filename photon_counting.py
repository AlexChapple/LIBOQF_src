"""
Photon counting distribution with statistics calculated 

"""

import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib
import colours
matplotlib.rcParams.update({'font.size': 24})

# Variables 
directory = "results/N80_phi_pi/"
photon_bin_cut_off = 25
num_of_simulations = 100000

photon_data = np.loadtxt(directory + "photon_counting_total.txt", delimiter=",")

# Photon counting distribution plots 

fig1 = plt.figure(1)
fig1.set_size_inches(18.5, 10.5)
fig1.set_alpha(0)
fig1.set_facecolor("none")
ax1 = plt.axes()
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_color(colours.spanish_gray)
ax1.spines['bottom'].set_color(colours.spanish_gray)
ax1.tick_params(axis='x', colors=colours.spanish_gray)
ax1.tick_params(axis='y', colors=colours.spanish_gray)
ax1.xaxis.label.set_color(colours.spanish_gray)
ax1.yaxis.label.set_color(colours.spanish_gray)

photon_data_norm = [i / num_of_simulations for i in photon_data]
x_list = [i for i in range(len(photon_data_norm))]

odd_list = []
odd_x_list = []
even_list = []
even_x_list = []

for i in range(len(x_list)):
    if i % 2 == 0:
        even_list.append(photon_data_norm[i])
        even_x_list.append(i)
    else:
        odd_list.append(photon_data_norm[i])
        odd_x_list.append(i)

# plt.bar(x_list, photon_data_norm, color=colours.greek_blue)
# plt.bar(even_x_list, even_list, color=colours.greek_red, label="even")
# plt.bar(odd_x_list, odd_list, color=colours.greek_blue, label="odd")
plt.bar(x_list[0:photon_bin_cut_off], photon_data_norm[0:photon_bin_cut_off])
# plt.xticks(range(0,photon_bin_cut_off))
# plt.xticks(fontsize=17)
plt.xlabel("Photon count")
plt.ylabel("Frequency (normalised)")
plt.legend()
# plt.savefig(directory + "photon_counting.pdf", facecolor=fig1.get_facecolor(), transparent=True, dpi=600)


# Do statistics here 
nbar = 0 
for i in range(len(x_list)):

    nbar += x_list[i] * photon_data_norm[i]

variance = 0 
for i in range(len(x_list)):

    variance += ((x_list[i] - nbar)**2) * photon_data_norm[i]

Mandel_Q = (variance - nbar)/ nbar 

print(nbar, Mandel_Q)