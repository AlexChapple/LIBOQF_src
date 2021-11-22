"""
Plots the single trajectory version 

"""

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
ax.text(0.7, 0.35, s="A", weight="bold", fontsize=19)
ax.plot(1.55, 0.78, 'o', fillstyle='none', markersize=35, linewidth=10, c=colours.greek_blue)
ax.text(1.52, 0.83, s="B", weight="bold", fontsize=19)
ax.plot(4.152, 0.464, 'o', fillstyle='none', markersize=35, linewidth=10, c=colours.greek_blue)
ax.text(4.1, 0.38, s="C", weight="bold", fontsize=19)

plt.savefig(directory + "single_trajectory_excited.pdf", dpi=600)

### ----- Plot single emission ----------------------------------

emission_data = np.loadtxt(directory + "emission_tracking.txt")

fig2 = plt.figure(2)
fig2.set_size_inches(18.5, 10.5)
fig2.set_alpha(0)
fig2.set_facecolor("none")
ax2 = plt.axes()
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_color(colours.spanish_gray)
ax2.spines['bottom'].set_color(colours.spanish_gray)
ax2.tick_params(axis='x', colors=colours.spanish_gray)
ax2.tick_params(axis='y', colors="none")
ax2.xaxis.label.set_color(colours.spanish_gray)
ax2.yaxis.label.set_color("none")
plt.xlabel("Time (seconds)")

names = ["A", "B", "C"]
for emissions in emission_data:

    plt.axvline(x = emissions, c=colours.sizzling_red, lw=3)
    plt.text(x=emissions+0.075, y=0.95, fontsize=34, weight="bold", s=names.pop(0))

plt.savefig(directory + "single_trajectory_emissions.pdf", dpi=600, bbox_inches='tight')


