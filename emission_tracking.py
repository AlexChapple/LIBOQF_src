import numpy as np 
import matplotlib.pyplot as plt 
import colours

directory = "results/N80_phi_pi/"
emission_data = np.loadtxt(directory + "emission_tracking_total.txt")

# Testing emission data 
# emission_data = [
#     1,
#     1.01,
#     1.02,
#     150,
#     34,
#     34.05,
#     34.14,
#     150,
#     150,
#     54,
#     150,
#     89,
#     89.1
# ]

tau = 0.2 
end_time = 100
num_of_sim = 100000

total_photon_numbers = 0 

emission_count_list = [0 for i in range(7)]

session_count = 0 
session_start_time = None

file_length = max(range(len(emission_data)))

for index in range(len(emission_data)):

    if session_start_time == None and emission_data[index] != end_time + 50: # Initialises the very first emission, starts first session

        session_start_time = emission_data[index] 
        session_count = 1 
        total_photon_numbers += 1

    elif session_start_time == None and emission_data[index] == end_time + 50:

        pass 

    else: # not the first emission 

        if emission_data[index] == end_time + 50: # means a new simulation has begun, start new session

            emission_count_list[session_count-1] += 1

            session_count = 0
            session_start_time = None 

        else:

            waiting_time = emission_data[index] - session_start_time # finds time between the current and previous emissions

            if waiting_time <= tau: # within round trip time, then same session

                session_count += 1
                total_photon_numbers += 1 

            else: # Not within the same session time

                emission_count_list[session_count-1] += 1

                session_count =  1
                session_start_time = emission_data[index]
                total_photon_numbers += 1

    # if index == file_length: # checks if its the last index, if so, stores the current session count 

    #     emission_count_list[session_count-1] += 1

    if index % 1000 == 0:
        print("indexed over " + str(index) + " simulations.")
    

x_list = range(len(emission_count_list))


print(total_photon_numbers)

total = 0 
for i in range(len(emission_count_list)):
    
    total += ((i+1) * emission_count_list[i])

print(total)

total_session_number = sum(emission_count_list)

normalised_emission_count_list = [i / total_session_number for i in emission_count_list]
plt.bar(x_list, normalised_emission_count_list)
plt.show()

print(normalised_emission_count_list)