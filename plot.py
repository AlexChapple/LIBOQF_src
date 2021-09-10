import os 
import matplotlib.pyplot as plt
import matplotlib
import numpy as np 
# matplotlib.use('Agg')

# Parameters
num_of_dir = 50

initialised = 0
photon_list = []
time_list = []

directory = "results/Omega_10_tau_01_phi_0"

photon_data = np.loadtxt(directory + "/photon_counting_total.txt")
spin_down_data_total = np.loadtxt(directory + "/spin_up_total.txt", delimiter=",")

time_list = spin_down_data_total[:,0]
spin_down_data = spin_down_data_total[:,1]

x = x_list = [i for i in range(0,40)]
spin_down_data = [i / num_of_dir for i in spin_down_data]

# matplotlib.rcParams.update({'font.size': 40})
# px = 1/plt.rcParams['figure.dpi']
plt.figure()
# plt.figure(figsize=(1400*1.7*px, 2*427*1.7*px))
plt.bar(x, photon_data[0:40], color="hotpink")
plt.xlabel("Photon Number", fontsize=22)
plt.ylabel("frequency (a.u)", fontsize=22)
plt.title("photon counting distribution")
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
# plt.savefig(directory + "/photon_counting_trim.png", dpi=600)
# plt.savefig("pcd.png", transparent=True, dpi=600)
plt.show()

px = 1/plt.rcParams['figure.dpi']
plt.figure(figsize=(528*1.7*px, 427*1.7*px))
plt.plot(time_list, spin_down_data, linewidth=3)
plt.grid()
plt.xlabel("Time")
plt.ylabel("Spin down probability")
plt.xticks(np.arange(min(time_list), max(time_list)+1, 1.0))
plt.yticks(np.arange(np.floor(np.min(spin_down_data)), np.ceil(np.max(spin_down_data)), 0.25))
plt.show()
# title = "$\\tau = 0.2$, dt=0.002, $\\phi=\pi$, N=20, Samples=25000, $\\Omega = 10\pi$, $\\gamma_R = \\gamma_L = 0.5$"

# plt.title(title)
# plt.savefig(directory + "/spin_down_trim.png", dpi=600)
# plt.savefig("../../temp/Figure_4.pdf")

