"""
Emission tracking code

"""

# Import libraries 
import numpy as np 
import matplotlib.pyplot as plt 
import colours
import matplotlib

# Import data 
directory = "results/N80_phi_0/"
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

# Simulation parameters 
tau = 0.2 
end_time = 100
num_of_sim = 100000

emission_count_list = [0 for i in range(5)]

session_count = 0 
total_photon_numbers = 0 
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

    if index % 1000 == 0:
        print("indexed over " + str(index) + " simulations.")

# print(total_photon_numbers)

# total = 0 
# for i in range(len(emission_count_list)):
    
#     total += ((i+1) * emission_count_list[i])

# print(total)    

# ----- Plotting -------------------------------------------------------------------------------
x_list = range(1,len(emission_count_list)+1)

total_session_number = sum(emission_count_list)
normalised_emission_count_list = [i / total_session_number for i in emission_count_list]

matplotlib.rcParams.update({'font.size': 18})
fig = plt.figure()
fig.set_size_inches(18.5, 10.5)
fig.set_alpha(0)
fig.set_facecolor("none")
ax = plt.axes()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(colours.spanish_gray)
ax.spines['bottom'].set_color(colours.spanish_gray)
ax.tick_params(axis='x', colors=colours.spanish_gray)
ax.tick_params(axis='y', colors=colours.spanish_gray)
ax.xaxis.label.set_color(colours.spanish_gray)
ax.yaxis.label.set_color(colours.spanish_gray)
fig.set_alpha(0)
fig.set_facecolor("none")
plt.grid(alpha=0.25)

def emission_word_find(i):

    if i == 1:
        return "single"
    elif i == 2:
        return "pair"
    elif i == 3:
        return "triple"
    elif i == 4:
        return "quadruple"
    elif i == 5:
        return "quintuple"

for i in range(len(x_list)):

    if i == 1:
        c = colours.greek_red
    else:
        c = colours.greek_blue

    bar = plt.bar(x_list[i], normalised_emission_count_list[i], color=c)

    yval = bar[0].get_height()
    emission_word = emission_word_find(x_list[i])

    # plt.text(x_list[i], yval+0.01, "Probability of " + emission_word + "\nemission: " + str(round(normalised_emission_count_list[i] * 100, 3)) + "%", fontsize=16, horizontalalignment="center", c="black")

    plt.text(x_list[i], yval+0.01, str(round(normalised_emission_count_list[i] * 100, 3)) + "%", fontsize=20, horizontalalignment="center", c="black")

plt.xlabel("Photon Emission")
plt.ylabel("frequency")
plt.savefig(directory + "emission_tracking.pdf", facecolor=fig.get_facecolor(), transparent=True, dpi=600)