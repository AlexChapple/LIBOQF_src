### Summarises the data from all directories and makes plots 

import os 
import matplotlib.pyplot as plt
import matplotlib
import numpy as np 
from shutil import copy2 
matplotlib.use('Agg')

# Parameters
num_of_dir = 200

initialised = 0
input_file_copied = 0
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

        # Copy over input file if not done yet
        if input_file_copied == 0:
            src = working_dir + "input.txt"
            dst = "summary/input.txt"
            copy2(src,dst)
            input_file_copied = 1

        print(str(i) + " directories summarised.")

spin_up_list = spin_up_list / num_of_dir
spin_down_list = spin_down_list / num_of_dir
            

# ----- Write the respective data to npy files --------------------------------------------------------------------------------------------------

working_dir = "summary/"

np.save(file="{}spin_up_total.npy".format(working_dir), arr=spin_up_list)
np.save(file="{}spin_down_total.npy".format(working_dir), arr=spin_down_list)
np.save(file="{}photon_counting_total.npy".format(working_dir), arr=photon_list)

# with open(working_dir + "spin_up_total.txt", "w") as f:
#     for i in range(len(spin_up_list)):
#         data = str(time_list[i]) + "," + str(spin_up_list[i]) + "\n"
#         f.write(data)

# with open(working_dir + "spin_down_total.txt", "w") as f:
#     for i in range(len(spin_down_list)):
#         data = str(time_list[i]) + "," + str(spin_down_list[i]) + "\n"
#         f.write(data)

# with open(working_dir + "photon_counting_total.txt", "w") as f:
#     for i in range(len(photon_list)):
#         f.write(str(photon_list[i]) + "\n")

