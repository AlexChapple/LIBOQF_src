import numpy as np 
import matplotlib.pyplot as plt 

# Import data 
emission_data = np.loadtxt("results_test/tau_12/emission_tracking.txt")

photon_data_before = [0 for i in range(0,100)]
photon_data_after = [0 for i in range(0,100)]
photon_data = [0 for i in range(0,100)]

duration = 20
tau = 1.2
photon_count_before = 0
photon_count_after = 0 
photon_count = 0 
for emission in emission_data:

    if emission != duration + 50:

        if emission >= tau:
            
            photon_count_after += 1 
            photon_count += 1 

        else: 

            photon_count_before += 1 
            photon_count += 1 

    else:

        photon_data_before[photon_count_before] += 1 
        photon_data_after[photon_count_after] += 1
        photon_data[photon_count] += 1 
        photon_count_before = 0
        photon_count_after = 0  
        photon_count = 0 

plt.figure(1)
plt.bar(range(0,100), photon_data_before)
plt.title("before")

plt.figure(2)
# Separate to even and odd 
even = [0 for i in range(0,100)]
odd = [0 for i in range(0,100)]

for i in range(len(photon_data_after)):

    if i % 2 == 0:
        even[i] = photon_data_after[i]

    else:
        odd[i] = photon_data_after[i]

plt.bar(range(0,100), even, color="red", label="even")
plt.bar(range(0,100), odd, color="blue", label="odd")
plt.title("after")
plt.legend()

plt.figure(3)
plt.bar(range(0,100), photon_data)
plt.title("all")

plt.show()