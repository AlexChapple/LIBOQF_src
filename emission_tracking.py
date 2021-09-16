"""
Emission tracking 
"""

import numpy as np 
import matplotlib.pyplot as plt 

emission_data = np.loadtxt("emission_tracking_experimental.txt")

tau = 0.2 

single_emission_count = 0 
double_emission_count = 0
triple_emission_count = 0 

new_emission_session = True 
session_start_time = 0 
session_count = 0

for index in range(len(emission_data)):

    if index == 0:

        new_emission_session = False
        session_count += 1 
        session_start_time = emission_data[index]

    else:

        if emission_data[index] > emission_data[index - 1]:

            if emission_data[index] - session_start_time <= tau:

                session_count += 1 

            else:

                new_emission_session = True
                session_start_time = emission_data[index]

                if session_count == 1:
                    single_emission_count += 1 
                elif session_count == 2:
                    double_emission_count += 1 
                elif session_count == 3:
                    triple_emission_count += 1 
                else:
                    print("error, too many session counts")

        else:

            # New simulation 

            new_emission_session = True 
            session_start_time = emission_data[index]
            session_count = 1 

            if session_count == 1:
                single_emission_count += 1 
            elif session_count == 2:
                double_emission_count += 1 
            elif session_count == 3:
                triple_emission_count += 1 
            else:
                print("error, too many session counts")

    
                


print(single_emission_count)
print(double_emission_count)
print(triple_emission_count)


