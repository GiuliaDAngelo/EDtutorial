from bimvee.importIitYarp import importIitYarp
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('TkAgg')

events = importIitYarp(filePathOrName="data", tsBits=30)
e_x = events['data']['left']['dvs']['x']
e_y = events['data']['left']['dvs']['y']
e_ts = np.multiply(events['data']['left']['dvs']['ts'], 10**3)
e_pol = events['data']['left']['dvs']['pol']

width = 304
height = 240
window_period = 1 #ms
window = np.zeros((height,width))

for x, y, ts, pol in zip(e_x, e_y, e_ts, e_pol):
    if ts<=window_period:
        window[y][x]=1
    else:
        plt.imshow(window)
        plt.draw()
        plt.pause(0.2)
        matrix_events = np.zeros((height, width))
        window_period += window_period
        window = np.zeros((height, width))


print('end')