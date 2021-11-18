# Calculates the waiting time distribution from the total emission tracking file 
# 
# Author: Alex Chapple 

import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib
import colours
from mpl_toolkits.axes_grid1.inset_locator import (inset_axes, InsetPosition, mark_inset)

directory = "results/N80_phi_pi/"
num_of_simulations = 100000
emission_data = np.loadtxt(directory + "emission_tracking_total.txt")

# NOTE: This has to be changed each time you change the tracking file 
tau = 0.2
end_time = 100
increment = 20  
bin_width = tau / increment 

# Initialise arrays
waiting_time_list = np.zeros(int(np.ceil(end_time/bin_width)))
reduced_time_list = np.linspace(0,end_time,int(np.ceil(end_time/bin_width)))


### --- Sort the waiting time ------------------------------------------------------------------------------------------------ 

last_time = None # Starts with none
simulation_counter = 0 # Counts the number of simulation to make sure code is working, and hasn't skipped anything 
new_sim = True

for emission in emission_data:

    if emission == end_time + 50: # This is what I've added to make sure the code knows when a new simulation has started
        new_sim = True
        simulation_counter += 1 

    else:

        if new_sim == True: # means we are in a new simulation, need to update last time for the first case

            last_time = emission
            new_sim = False 

        else: 

            waiting_time = emission - last_time # Finds the waiting time for this emission 

            index = int(np.floor(waiting_time / bin_width)) # Finds the correct array to put it into 

            waiting_time_list[index] += 1 # Increases the histogram by one 

            last_time = emission # Updates the last time found for the next emission 


### --- Plotting ------------------------------------------------------------------------------------------------------------

matplotlib.rcParams.update({'font.size': 24})

# Plots the total waiting time distribution 
fig1, ax1 = plt.subplots()
fig1.set_size_inches(18.5, 10.5)
fig1.set_alpha(0)
fig1.set_facecolor("none")
# ax1 = plt.axes()
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_color(colours.spanish_gray)
ax1.spines['bottom'].set_color(colours.spanish_gray)
ax1.tick_params(axis='x', colors=colours.spanish_gray)
ax1.tick_params(axis='y', colors=colours.spanish_gray)
ax1.xaxis.label.set_color(colours.spanish_gray)
ax1.yaxis.label.set_color(colours.spanish_gray)

waiting_time_norm = [i / num_of_simulations for i in waiting_time_list]

ax1.bar(reduced_time_list, waiting_time_norm, width=0.01, color=colours.greek_blue)
ax1.set_xlabel("Waiting time (seconds)")
ax1.set_ylabel("Frequency (normalised)")
ax1.text(6,0.255,"(a)", fontsize=22, horizontalalignment="center", c="black")

# ax2 = plt.axes([0,0,1,1])
# ip = InsetPosition(ax1, [0.25,0.4,0.5,0.5])
# ax2.set_axes_locator(ip)
# mark_inset(ax1, ax2, loc1=3, loc2=4, fc="none", ec='0.5')
# ax2.bar(reduced_time_list[increment + 2:-1], waiting_time_norm[increment + 2:-1], width=0.0075, color=colours.greek_blue)

# Insert inset 
ax2 = inset_axes(ax1, width="65%", height="65%", loc=1)
ax2.bar(reduced_time_list[increment + 2:-1], waiting_time_norm[increment + 2:-1], width=0.0075, color=colours.greek_blue)
ax2.text(90,0.00175,"(b)", fontsize=22, horizontalalignment="center", c="black")
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_color(colours.spanish_gray)
ax2.spines['bottom'].set_color(colours.spanish_gray)
ax2.tick_params(axis='x', colors=colours.spanish_gray)
ax2.tick_params(axis='y', colors=colours.spanish_gray)
ax2.xaxis.label.set_color(colours.spanish_gray)
ax2.yaxis.label.set_color(colours.spanish_gray)
plt.xticks([0.2,20,40,60,80,100])

plt.savefig(directory + "waiting_time.pdf", facecolor=fig1.get_facecolor(), transparent=True, dpi=600)

# # Plots the waiting time distribution before tau 
# fig2 = plt.figure(2)
# fig2.set_size_inches(18.5, 10.5)
# fig2.set_alpha(0)
# fig2.set_facecolor("none")
# ax2 = plt.axes()
# ax2.spines['top'].set_visible(False)
# ax2.spines['right'].set_visible(False)
# ax2.spines['left'].set_color(colours.spanish_gray)
# ax2.spines['bottom'].set_color(colours.spanish_gray)
# ax2.tick_params(axis='x', colors=colours.spanish_gray)
# ax2.tick_params(axis='y', colors=colours.spanish_gray)
# ax2.xaxis.label.set_color(colours.spanish_gray)
# ax2.yaxis.label.set_color(colours.spanish_gray)

# plt.bar(reduced_time_list[0:increment + 2], waiting_time_norm[0:increment + 2], width=0.0075, color=colours.greek_blue)
# plt.xlabel("Waiting Time (seconds)")
# plt.ylabel("Frequency (Normalised)")
# plt.savefig(directory + "waiting_time_before.pdf", facecolor=fig1.get_facecolor(), transparent=True, dpi=600)

# # Plots the waiting time distribution after tau 
# fig3 = plt.figure(3)
# fig3.set_size_inches(18.5, 10.5)
# fig3.set_alpha(0)
# fig3.set_facecolor("none")
# ax3 = plt.axes()
# ax3.spines['top'].set_visible(False)
# ax3.spines['right'].set_visible(False)
# ax3.spines['left'].set_color(colours.spanish_gray)
# ax3.spines['bottom'].set_color(colours.spanish_gray)
# ax3.tick_params(axis='x', colors=colours.spanish_gray)
# ax3.tick_params(axis='y', colors=colours.spanish_gray)
# ax3.xaxis.label.set_color(colours.spanish_gray)
# ax3.yaxis.label.set_color(colours.spanish_gray)

# plt.bar(reduced_time_list[increment + 2:-1], waiting_time_norm[increment + 2:-1], width=0.0075, color=colours.greek_blue)
# plt.xlabel("Waiting Time (seconds)")
# plt.ylabel("Frequency (Normalised)")
# plt.savefig(directory + "waiting_time_after.pdf", facecolor=fig1.get_facecolor(), transparent=True, dpi=600)

