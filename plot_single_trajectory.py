"""
Plots the single trajectory version 

"""

from matplotlib import colors
import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib
import colours

matplotlib.rcParams.update({'font.size': 24})

directory = "results/single_tau_01/"

spin_up_data = np.loadtxt(directory + "spin_up_good.txt")

time_list = spin_up_data[:,0]
spin_up_data = spin_up_data[:,1]
half_way_data = [0.5 for i in time_list]

fig = plt.figure(1)
fig.set_size_inches(18.5, 10.5)
fig.set_alpha(0)
fig.set_facecolor("none")
ax = plt.axes()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(colours.spanish_gray)
ax.spines['bottom'].set_color(colours.spanish_gray)
ax.tick_params(axis='x', colors=colours.spanish_gray)
ax.tick_params(axis='y', colors=colours.spanish_gray)
ax.xaxis.label.set_color(colours.spanish_gray)
ax.yaxis.label.set_color(colours.spanish_gray)

plt.plot(time_list, spin_up_data, linewidth=3, c=colours.sizzling_red)
plt.grid()
# plt.legend()
plt.xlabel("time (seconds)")
plt.ylabel("Excited State Probability $P_{+}(t)$")

# Add text 
ax.plot(0.757, 0.418, 'o', fillstyle='none', markersize=35, linewidth=10, c=colours.greek_blue)
ax.plot(1.559, 0.78, 'o', fillstyle='none', markersize=35, linewidth=10, c=colours.greek_blue)
ax.plot(4.152, 0.464, 'o', fillstyle='none', markersize=35, linewidth=10, c=colours.greek_blue)

plt.savefig(directory + "single_trajectory.pdf", dpi=600)