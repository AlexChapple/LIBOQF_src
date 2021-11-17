# Set up n number of folders in the directory and copies over relevant files 

import os 
from shutil import copy2

# Number of directories wanted
num_of_dirs = 50

# Make data folder, that holds all the smaller directories 
os.mkdir("data")

# Make other folders 
os.mkdir("summary")
os.mkdir("slurm_folder")

for i in range(num_of_dirs):

    os.mkdir("data/" + str(i))

    working_dir = "data/" + str(i) + "/"

    # Copy in files for this simulation 
    src = "LIBOQF"
    dst = working_dir + "LIBOQF"
    copy2(src,dst)

    # make empty files for writing in each directory 
    open(working_dir + "log.txt", "a+").close()
    open(working_dir + "input.txt", "a+").close()
    open(working_dir + "spin_down.txt", "a+").close()
    open(working_dir + "spin_up.txt", "a+").close()
    open(working_dir + "photon_counting.txt", "a+").close()
    open(working_dir + "emission_tracking.txt", "a+").close()
    

