import numpy as np 
import matplotlib.pyplot as plt 

emission_data = np.loadtxt("experimental/emission_tracking_e.txt")

tau = 0.2 
end_time = 100
bin_width = tau / 10 

waiting_time_list = np.zeros(int(np.ceil(end_time/bin_width)))
reduced_time_list = np.linspace(0,100,int(np.ceil(end_time/bin_width)))

### Sort the waiting time ### 

last_time = None 
simulation_counter = 0
new_sim = True

for emission in emission_data:

    if emission == end_time + 50:
        new_sim = True
        simulation_counter += 1 

    else:

        if new_sim == True: # means we are in a new simulation, need to update last time for the first case

            last_time = emission
            new_sim = False 

        else: 

            waiting_time = emission - last_time

            index = int(np.floor(waiting_time / bin_width))

            waiting_time_list[index] += 1 

            last_time = emission

plt.bar(reduced_time_list, waiting_time_list)
plt.show()