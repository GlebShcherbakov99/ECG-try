import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

def animate(i):
    data = pd.read_csv('data.csv')
    x = data['frame']
    y1 = data['diff1']
    y2 = data['diff2']
    y3 = data['diff3']
    y4 = data['diff4']
    plt.cla()

    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')
    plt.plot(x, y3, label='Channel 3')
    plt.plot(x, y4, label='Channel 4')

    plt.legend(loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()

