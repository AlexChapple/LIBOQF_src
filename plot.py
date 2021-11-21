# The plotting file for production 

from matplotlib import colors
import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib
import colours

# Variables 
directory = "results/N80_phi_pi/"
photon_bin_cut_off = 25
end_time = 7
tau = 0.2
num_of_simulations = 100000

delimiter = ","
single_trajectory = False 

spin_down_data = np.loadtxt(directory + "spin_down_total.txt", delimiter=delimiter)
spin_up_data = np.loadtxt(directory + "spin_up_total.txt", delimiter=delimiter)
photon_data = np.loadtxt(directory + "photon_counting_total.txt", delimiter=delimiter)[0:photon_bin_cut_off]
if single_trajectory == True:
    emission_tracking_data = np.loadtxt(directory + "emission_tracking_total.txt", delimiter=delimiter)

matplotlib.rcParams.update({'font.size': 24})

# Spin down plots 
time_list = spin_down_data[:,0]
half_way_data = [0.5 for i in time_list]
spin_down_data = spin_down_data[:,1]

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

plt.plot(time_list, spin_down_data, linewidth=3, c=colours.greek_blue, label="Ground state")
plt.plot(time_list, half_way_data, c="black", linestyle = 'dashed', label="Probability = 0.5")
plt.grid()
plt.xlabel("time (seconds)")
plt.ylabel("Ground State Probability $P_{-}$")
plt.legend()
plt.savefig(directory+"ground_state.pdf", facecolor=fig1.get_facecolor(), transparent=True, dpi=600)

# Spin up plots 
spin_up_data = spin_up_data[:,1]

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
ax2.tick_params(axis='y', colors=colours.spanish_gray)
ax2.xaxis.label.set_color(colours.spanish_gray)
ax2.yaxis.label.set_color(colours.spanish_gray)

plt.plot(time_list, spin_up_data, linewidth=3, c=colours.sizzling_red, label="Excited state")
plt.plot(time_list, half_way_data, c="black", linestyle = 'dashed', label="Probability = 0.5")

if single_trajectory == True:

    ax2.plot(2.34,0.41,'o',fillstyle='none',markersize=35, linewidth=10, c=colours.greek_blue)
    ax2.plot(3.67,0.035,'o',fillstyle='none',markersize=35, linewidth=10, c=colours.greek_blue)
    ax2.plot(6.75,0.19,'o',fillstyle='none',markersize=35, linewidth=10, c=colours.greek_blue)
    # ax2.annotate('', xy=(2.3, 0.39), xytext=(3, 0.25),
    #     arrowprops=dict(facecolor='black', shrink=0.05))

    # ax2.annotate('', xy=(3.65, 0.01), xytext=(3, 0.01),
    #     arrowprops=dict(facecolor='black', shrink=0.05))

    # ax2.annotate('', xy=(6.8, 0.18), xytext=(6.1, 0.01),
    #     arrowprops=dict(facecolor='black', shrink=0.05))

plt.grid()
plt.legend()
plt.xlabel("time (seconds)")
plt.ylabel("Excited State Probability $P_{+}$")
plt.savefig(directory+"excited_state.pdf", facecolor=fig1.get_facecolor(), transparent=True, dpi=600)

# Spin up and down on the same figure 

fig3 = plt.figure(3)
fig3.set_size_inches(18.5, 10.5)
fig3.set_alpha(0)
fig3.set_facecolor("none")
ax3 = plt.axes()
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.spines['left'].set_color(colours.spanish_gray)
ax3.spines['bottom'].set_color(colours.spanish_gray)
ax3.tick_params(axis='x', colors=colours.spanish_gray)
ax3.tick_params(axis='y', colors=colours.spanish_gray)
ax3.xaxis.label.set_color(colours.spanish_gray)
ax3.yaxis.label.set_color(colours.spanish_gray)

plt.plot(time_list, spin_down_data, linewidth=3, c=colours.greek_blue, label="Ground state")
plt.plot(time_list, spin_up_data, linewidth=3, c=colours.sizzling_red, label="Excited state")
plt.plot(time_list, half_way_data, c="black", linestyle = 'dashed', label="Probability = 0.5")
plt.grid()
plt.xlabel("time (seconds)")
plt.ylabel("Probability")
plt.legend()
plt.savefig(directory + "probability.pdf", facecolor=fig1.get_facecolor(), transparent=True, dpi=600)

# Emission tracking plots (for single trajectories only)

if single_trajectory == True:

    fig4 = plt.figure(4)
    fig4.set_size_inches(18.5, 10.5)
    fig4.set_alpha(0)
    fig4.set_facecolor("none")
    ax4 = plt.axes()
    ax4.spines['top'].set_visible(False)
    ax4.spines['right'].set_visible(False)
    ax4.spines['left'].set_color(colours.spanish_gray)
    ax4.spines['bottom'].set_color(colours.spanish_gray)
    ax4.tick_params(axis='x', colors=colours.spanish_gray)
    ax4.tick_params(axis='y', colors=colours.spanish_gray)
    ax4.xaxis.label.set_color(colours.spanish_gray)
    ax4.yaxis.label.set_color(colours.spanish_gray)

    plt.xlim([0,7])
    plt.xlabel("Time (seconds)")
    plt.ylabel("Emissions")

    for emissions in emission_tracking_data:
        plt.axvline(x = emissions, c=colours.sizzling_red)

    plt.savefig(directory + "emissions.pdf", facecolor=fig1.get_facecolor(), transparent=True, dpi=600)

# Photon counting distribution plots 
fig5 = plt.figure(5)
fig5.set_size_inches(18.5, 10.5)
fig5.set_alpha(0)
fig5.set_facecolor("none")
ax5 = plt.axes()
ax5.spines['top'].set_visible(False)
ax5.spines['right'].set_visible(False)
ax5.spines['left'].set_color(colours.spanish_gray)
ax5.spines['bottom'].set_color(colours.spanish_gray)
ax5.tick_params(axis='x', colors=colours.spanish_gray)
ax5.tick_params(axis='y', colors=colours.spanish_gray)
ax5.xaxis.label.set_color(colours.spanish_gray)
ax5.yaxis.label.set_color(colours.spanish_gray)

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
plt.bar(even_x_list, even_list, color=colours.greek_red, label="even")
plt.bar(odd_x_list, odd_list, color=colours.greek_blue, label="odd")
plt.xticks(range(0,photon_bin_cut_off))
plt.xticks(fontsize=17)
plt.xlabel("Photon count")
plt.ylabel("Frequency (normalised)")
plt.legend()
plt.savefig(directory + "photon_counting.pdf", facecolor=fig1.get_facecolor(), transparent=True, dpi=600)

# Do photon statistics here 
nbar = 0 
for i in range(len(x_list)):

    nbar += x_list[i] * photon_data_norm[i]

variance = 0 
for i in range(len(x_list)):

    variance += ((x_list[i] - nbar)**2) * photon_data_norm[i]

Mandel_Q = (variance - nbar)/ nbar 

print("$\\overbar{n}$ = ", nbar)
print("Q = ", Mandel_Q)

# Add a poisson distribution curve onto the plot 
poisson_list = []
for k in x_list:

    p = (nbar ** k) * np.exp(-nbar) / np.math.factorial(k)
    poisson_list.append(p)

plt.plot(x_list[0:photon_bin_cut_off], poisson_list[0:photon_bin_cut_off], alpha=0.5)
plt.savefig(directory + "photon_counting_poisson.pdf", facecolor=fig5.get_facecolor(), transparent=True, dpi=600)