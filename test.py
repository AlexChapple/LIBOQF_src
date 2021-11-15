import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib
import colours

directory = "results/N80/"
num_of_simulations = 100000

photon_data = np.loadtxt(directory + "photon_counting_total.txt")

matplotlib.rcParams.update({'font.size': 24})
fig5 = plt.figure(5)
fig5.set_size_inches(18.5, 10.5)
ax5 = plt.axes()
ax5.spines['top'].set_visible(False)
ax5.spines['right'].set_visible(False)
ax5.spines['left'].set_color(colours.spanish_gray)
ax5.spines['bottom'].set_color(colours.spanish_gray)
ax5.tick_params(axis='x', colors=colours.spanish_gray)
ax5.tick_params(axis='y', colors=colours.spanish_gray)
ax5.xaxis.label.set_color(colours.spanish_gray)
ax5.yaxis.label.set_color(colours.spanish_gray)

photon_data_norm = [i / num_of_simulations for i in photon_data[0:30]]

x_list = [i for i in range(len(photon_data_norm))]

even_list = []
even_data_list = []
odd_list = []
odd_data_list = []

for i in x_list:

    if i % 2 == 0:
        even_list.append(i)
        even_data_list.append(photon_data_norm[i])
    else:
        odd_list.append(i)
        odd_data_list.append(photon_data_norm[i])

plt.bar(even_list, even_data_list, color=colours.greek_red, label="Even peaks")
plt.bar(odd_list, odd_data_list, color=colours.greek_blue, label="Odd peaks")
plt.ylabel("Frequency (Normalised)")
plt.xlabel("Photon Number")
plt.legend()
plt.show()
