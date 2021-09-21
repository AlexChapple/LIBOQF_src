"""
Emission tracking 
"""

import numpy as np 
import matplotlib.pyplot as plt 
import colours 
import matplotlib

emission_data = np.loadtxt("emission_tracking_total.txt")

tau = 0.2 
num_of_sim = 50000

single_emission_count = 0 
double_emission_count = 0
triple_emission_count = 0 
quadruple_emission_count = 0 

new_emission_session = True 
session_start_time = 0 
session_count = 0

for index in range(len(emission_data)):

    if index == 0:

        session_count += 1 
        session_start_time = emission_data[index]

    elif index == len(emission_data)-1:

        session_count += 1 

        if session_count == 1:
            single_emission_count += 1 
        elif session_count == 2:
            double_emission_count += 1 
        elif session_count == 3:
            triple_emission_count += 1 
        elif session_count == 4:
            quadruple_emission_count += 1 
        else:
            print("error, too many session counts")
    
    else:

        if emission_data[index] > emission_data[index-1]:

            if emission_data[index] - session_start_time <= tau:
                session_count += 1 
            
            else:
                # Means we've entered a new session in the same simulation 

                if session_count == 1:
                    single_emission_count += 1 
                elif session_count == 2:
                    double_emission_count += 1 
                elif session_count == 3:
                    triple_emission_count += 1 
                elif session_count == 4:
                    quadruple_emission_count += 1 
                else:
                    print("error, too many session counts")


                session_count = 1
                session_start_time = emission_data[index]

        else: # Means we've entered a new simulation 
            
            if session_count == 1:
                single_emission_count += 1 
            elif session_count == 2:
                double_emission_count += 1 
            elif session_count == 3:
                triple_emission_count += 1 
            elif session_count == 4:
                quadruple_emission_count += 1 
            else:
                print("error, too many session counts")


            session_count = 1
            session_start_time = emission_data[index]    
                

### Do some statistics here 
print("Number of single emissions ", single_emission_count)
print("Number of double emissions ", double_emission_count)
print("Number of triple emissions ", triple_emission_count)
print("Number of quadruple emissions ", quadruple_emission_count)

total_emission_count = single_emission_count + double_emission_count + triple_emission_count + quadruple_emission_count

prob_single = 100 * single_emission_count / total_emission_count
prob_double = 100 * (double_emission_count) / total_emission_count
prob_triple = 100 * ( triple_emission_count) / total_emission_count
prob_quadruple = 100 * quadruple_emission_count / total_emission_count

total_photon_count = single_emission_count + (2*double_emission_count) + (3*triple_emission_count) + (4*quadruple_emission_count)

print("Probability of single emission: ", prob_single)
print("Probability of double emission: ", prob_double)
print("Probability of triple emission: ", prob_triple)
print("Probability of quadruple emission: ", prob_quadruple)


### Make plots 
matplotlib.rcParams.update({'font.size': 18})
fig = plt.figure(1)
fig.set_size_inches(18.5, 10.5)
ax = plt.axes()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(colours.purple_new)
ax.spines['bottom'].set_color(colours.purple_new)
ax.tick_params(axis='x', colors=colours.spanish_gray)
ax.tick_params(axis='y', colors=colours.spanish_gray)
ax.xaxis.label.set_color(colours.spanish_gray)
ax.yaxis.label.set_color(colours.spanish_gray)
fig.set_alpha(0)
fig.set_facecolor("none")
plt.grid(alpha=0.25)
bars1 = plt.bar(1,single_emission_count,width=0.5,color=colours.french_violet, label="Single emission")
bars2 = plt.bar(2,double_emission_count,width=0.5,color=colours.pumpkin, label="Double emission")
bars3 = plt.bar(3,triple_emission_count,width=0.5,color=colours.french_violet, label="Triple emission")
bars4 = plt.bar(4,quadruple_emission_count,width=0.5,color=colours.french_violet, label="Quadruple emission")

# plt.bar([1,2,3], [single_emission_count, double_emission_count, triple_emission_count], width=0.5)

yval1 = bars1[0].get_height()
yval2 = bars2[0].get_height()
yval3 = bars3[0].get_height()
yval4 = bars4[0].get_height()

plt.text(1, yval1+5.75, "Probability of single\nemission: " + str(round(prob_single, 3)) + "%", fontsize=13, horizontalalignment="center", c="black")
plt.text(2, yval2+5.75, "Probability of double\nemission: " + str(round(prob_double, 3)) + "%", fontsize=13, horizontalalignment="center", c="black")
plt.text(3, yval3+5.75, "Probability of triple\nemission: " + str(round(prob_triple, 3)) + "%", fontsize=13, horizontalalignment="center", c="black")
plt.text(4, yval4+5.75, "Probability of quadruple\nemission: " + str(round(prob_quadruple, 3)) + "%", fontsize=13, horizontalalignment="center", c="black")

plt.xlabel("Photon Emission")
plt.ylabel("frequency")
# plt.legend()
plt.show()

print(total_photon_count)
print("avg number of photons per simulation: ", total_photon_count/num_of_sim)