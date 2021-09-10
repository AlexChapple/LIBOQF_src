### Summarises the data from all directories and makes plots 

import os 
import matplotlib.pyplot as plt
import matplotlib
import numpy as np 
matplotlib.use('Agg')

# Parameters
num_of_dir = 50
total_num_of_sim = 1

initialised = 0
spin_down_list = [] 
spin_up_list = [] 
photon_list = []
time_list = []

no_list = []

# ----- Go into each directory and copy over -----------------------------------------------------------------------------------------------------------------------

for i in range(num_of_dir):

    if i in no_list:
        pass
    else:

        working_dir = "data/" + str(i) + "/"    

        spin_up_data = np.loadtxt(working_dir + "spin_up.txt")
        spin_down_data = np.loadtxt(working_dir + "spin_down.txt")
        photon_data = np.loadtxt(working_dir + "photon_counting.txt")

        time_data = spin_up_data[:, 0]

        if initialised == 0:
            time_list = time_data 
            spin_down_list = np.zeros(len(spin_down_data[:,1]))
            spin_up_list = np.zeros(len(spin_up_data[:,1]))
            photon_list = np.zeros(len(photon_data))
            initialised = 1

        spin_up_data = spin_up_data[:,1]
        spin_down_data = spin_down_data[:,1]

        spin_up_list = spin_up_list + spin_up_data
        spin_down_list = spin_down_list + spin_down_data
        photon_list = photon_list + photon_data

        spin_up_list = spin_up_list / total_num_of_sim
        spin_down_list = spin_down_list / total_num_of_sim

        print(str(i) + " directories summarised.")
            

# ----- Write the respective data to files --------------------------------------------------------------------------------------------------

working_dir = "summary/"

with open(working_dir + "spin_up_total.txt", "w") as f:
    for i in range(len(spin_up_list)):
        data = str(time_list[i]) + "," + str(spin_up_list[i]) + "\n"
        f.write(data)

with open(working_dir + "spin_down_total.txt", "w") as f:
    for i in range(len(spin_down_list)):
        data = str(time_list[i]) + "," + str(spin_down_list[i]) + "\n"
        f.write(data)

with open(working_dir + "photon_counting_total.txt", "w") as f:
    for i in range(len(photon_list)):
        f.write(str(photon_list[i]) + "\n")


# ----- Plot the respective data ----------------------------------------------------------------------------------------------------------------------

plt.figure(1)
plt.plot(time_list, spin_down_list)
plt.xlabel("time (s)")
plt.ylabel("Probability spin down")
plt.savefig("figures/spin_down.png", dpi=600)

plt.figure(2)
plt.plot(time_list, spin_up_list)
plt.xlabel("time (s)")
plt.ylabel("Probability spin up")
plt.savefig("figures/spin_up.png", dpi=600)

plt.figure(3)
x_list = [i for i in range(len(photon_list))]
plt.bar(x_list, photon_list)
plt.xlabel("Photon Number")
plt.ylabel("frequency (a.u)")
plt.title("photon counting distribution")
plt.savefig("figures/photon_counting.png", dpi=600)