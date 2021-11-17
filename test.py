# Quick test to see if the number of odd vs even photons match the data 

import numpy as np 

photon_data = np.loadtxt("results/N80_phi_pi/photon_counting_total.txt")

even_total = 0
odd_total = 0

for i in range(len(photon_data)):

    if i % 2 == 0:
        even_total += photon_data[i]
    else:
        odd_total += photon_data[i]

total = sum(photon_data)

even_total /= total 
odd_total /= total 

print(even_total)
print(odd_total)