# Set up n number of folders in the directory and copies over relevant files 

import os 
from shutil import copy2

# Number of directories wanted
num_of_dirs = 200

# Make data folder, that holds all the smaller directories 
os.mkdir("data")

# Make other folders 
os.mkdir("summary")
os.mkdir("slurm_folder")

for i in range(num_of_dirs):

    os.mkdir("data/" + str(i))

    working_dir = "data/" + str(i) + "/"

    # Copy in files for this simulation 
    src = "LIBOQF_tau08"
    dst = working_dir + "LIBOQF_tau08"
    copy2(src,dst)

    # make empty files for writing input in each directory 
    open(working_dir + "input.txt", "a+").close()
    open(working_dir + "spin_down.dat", "a+").close()
    open(working_dir + "spin_up.dat", "a+").close()
    open(working_dir + "photon_counting.dat", "a+").close()
    open(working_dir + "emission_tracking.dat", "a+").close()
    

