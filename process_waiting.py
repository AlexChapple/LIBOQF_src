import matplotlib.pyplot as plt 
import numpy as np 
from math import floor
from math import factorial

waiting_time_data = np.loadtxt("results/Omega_10_tau_01_phi_pi/waiting_time_total.txt", delimiter=",")

waiting_time = waiting_time_data[:,0]
waiting_time_hist = waiting_time_data[:,1]

# Stuff before 0.2 seconds
waiting_time_first = waiting_time[0:10]
waiting_time_hist_first = waiting_time_hist[0:10]

plt.figure(1)
plt.bar(waiting_time_first, waiting_time_hist_first, width=0.01)

# lam = 0.1
# # Fitting a poisson distribution here 
# def poisson(k):

#     return (lam**k) * np.exp(-lam) / (factorial(k))

# poisson_list = [poisson(x) for x in waiting_time_hist_first]
# plt.plot(waiting_time_first, poisson_list)
# plt.show()


# Stuff after 0.2 seconds
end_time = 14
tau = 0.1 
waiting_time_last = waiting_time[11:-1]
waiting_time_hist_last = waiting_time_hist[11:-1]

bar_count = 30
reduced_waiting_time_last = np.linspace(tau,end_time,bar_count)
reduced_waiting_time_hist_last = np.zeros(bar_count)

increment = (end_time - tau) / bar_count

for i in range(len(waiting_time_last)):

    val = waiting_time_last[i] - tau
    c = floor(val/increment)

    reduced_waiting_time_hist_last[c] += waiting_time_hist_last[i]

plt.figure(2)
plt.bar(reduced_waiting_time_last, reduced_waiting_time_hist_last, width=2.5)


plt.figure(3)
# combined_waiting_time = np.concatenate((np.array(waiting_time_first), np.array(reduced_waiting_time_last)))
# combined_waiting_time_hist = np.concatenate((np.array(waiting_time_hist_first), np.array(reduced_waiting_time_hist_last)))
# plt.bar(combined_waiting_time, combined_waiting_time_hist,width=3)
plt.bar(waiting_time, waiting_time_hist)
plt.show()