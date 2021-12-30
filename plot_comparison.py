from matplotlib import colors
import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib
import colours

directory = "results/"

spin_down_1 = np.loadtxt(directory + "Omega_10_tau_02_phi_0" + "/spin_down_total.txt", delimiter=",")
spin_down_2 = np.loadtxt(directory + "N80_phi_0" + "/spin_down_total.txt", delimiter=",")

time_list = spin_down_1[:,0]
spin_down_1 = spin_down_1[:,1]
spin_down_2 = spin_down_2[:,1]

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

plt.plot(time_list, spin_down_1, c=colours.greek_blue, lw=3, label="N = 20")
plt.plot(time_list, spin_down_2, c=colours.greek_red, lw=3, label="N = 80", ls="dashdotted")

half_prob = [0.5 for t in time_list]
plt.plot(time_list, half_prob, ls="dotted", lw=3, label="Probability = 0.5")
