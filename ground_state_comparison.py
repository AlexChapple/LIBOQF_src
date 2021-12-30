"""

compare the results for pi = 0 between N = 20 and N = 80 cases.


"""

import numpy as np 
import matplotlib.pyplot as plt 
import colours
import matplotlib

matplotlib.rcParams.update({'font.size': 24})


directory1 = "results/Omega_10_tau_02_phi_0/"
directory2 = "results/N80_phi_0/"

spin_down_data1 = np.loadtxt(directory1 + "spin_down_total.txt", delimiter=",")
spin_down_data2 = np.loadtxt(directory2 + "spin_down_total.txt", delimiter=",")

time_list1 = spin_down_data1[:,0]
time_list2 = spin_down_data2[:,0]
half_way_data = [0.5 for i in time_list1]
spin_down_data1 = spin_down_data1[:,1]
spin_down_data2 = spin_down_data2[:,1]

fig = plt.figure()
fig.set_size_inches(18.5, 10.5)
fig.set_alpha(0)
fig.set_facecolor("none")
ax = plt.axes()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(colours.spanish_gray)
ax.spines['bottom'].set_color(colours.spanish_gray)
ax.spines['bottom'].set_color(colours.spanish_gray)
ax.tick_params(axis='y', colors=colours.spanish_gray)
ax.xaxis.label.set_color(colours.spanish_gray)
ax.yaxis.label.set_color(colours.spanish_gray)


plt.plot(time_list1, spin_down_data1, linewidth=3, c=colours.greek_blue, label="N = 20")
plt.plot(time_list2, spin_down_data2, linewidth=3, c=colours.greek_red, label="N = 80", linestyle="dashdot")
plt.plot(time_list1, half_way_data, c="black", linestyle="dashed", label="Probability = 0.5")

plt.grid()
plt.xlabel("$\gamma t$")
plt.ylabel("Ground state probability $P_{-}$")
plt.legend()
plt.savefig("ground_state_comparision.pdf", facecolor=fig.get_facecolor(), transparent=True, dpi=600)