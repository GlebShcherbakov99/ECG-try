import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.fftpack as fftpack
import statsmodels.api as sm
import corefunc as cf
from sqlalchemy import column
from scipy.fft import fft, fftfreq
from matplotlib.animation import FuncAnimation

df = cf.DFReadCSV('EXAMPLE.CSV')
time, voltage = cf.DFExtractData(df)
sig = cf.LowessSig(time, voltage, 0.005)

x, y = [], []
for i in range(len(time)-1):
    der = cf.DerivativeCheck(time[i],
                             time[i+1],
                             sig[i],
                             sig[i+1], coeff=3.2)
    if der == True:
        x.append(time[i])
        y.append(sig[i])

plt.subplot(2, 1, 1)
plt.plot(time, sig, linewidth=1.5, color='red')
plt.subplot(2, 1, 2)
plt.plot(x, y, linewidth=1.5, color='green')

plt.show()