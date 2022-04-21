### Summarises the emission data into one file 

import numpy as np 

num_of_dir = 200
initialised = False 
total_emission_data = np.array([])

for i in range(num_of_dir):

    working_dir = "data/" + str(i) + "/"

    emission_data = np.loadtxt(working_dir + "emission_tracking.txt")

    if initialised == False:

        total_emission_data = emission_data
        initialised = True

    else:

        total_emission_data = np.concatenate((total_emission_data, emission_data), axis=None)

    
# Write to a total txt file 
np.save(file="summary/emission_tracking_total.npy", arr=total_emission_data)

