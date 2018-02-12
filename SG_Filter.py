import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
import pandas as pd
import csv

# t = np.linspace(-4, 4, 500)
# y = np.exp( -t**2 ) + np.random.normal(0, 0.05, t.shape)
# ysg = savgol_filter(y, window_length=31, polyorder=4)
#
# plt.plot(t, y, label='Noisy signal')
# plt.plot(t, np.exp(-t**2), 'k', lw=1.5, label='Original signal')
# plt.plot(t, ysg, 'r', label='Filtered signal')
# plt.legend()
# plt.show()


# with open("time stamp.txt", 'rt') as f:
#     for data_point in f:
#


# data = np.loadtxt("time stamp.txt")
# filter_data = savgol_filter(data, window_length=31, polyorder=2)
# print(filter_data)


# data = pd.read_csv("data.csv")
# data.tail()
# print(data)


data = np.genfromtxt('data.csv', delimiter=',')
filter_data = savgol_filter(data[:, 1], window_length=301, polyorder=2, mode='nearest')
# print(filter_data)


plt.plot(data[:, 0], data[:, 1], label='Noisy signal')
plt.plot(data[:, 0], filter_data, 'r', label='Filtered signal')
plt.legend()
plt.show()