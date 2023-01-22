import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.fftpack as fftpack
import statsmodels.api as sm
import corefunc as cf
from sqlalchemy import column
from scipy.fft import fft, fftfreq
from scipy import signal
from matplotlib.animation import FuncAnimation

df = cf.DFReadCSV('ECG Gleb/GLEB.CSV')
time, voltage = cf.DFExtractData(df)

#sig = cf.LowessSig(time, voltage, 0.02)

#sigMF = medfilt(sig, kernel_size=3)

sos = signal.butter(150, 60, 'hp', fs=1000, output='sos')
filtered = signal.sosfilt(sos, voltage)

sigMF = signal.medfilt(voltage, kernel_size=7)

sig = cf.LowessSig(time, sigMF, 0.01)

freq, fourier = cf.FFTSig(voltage, 0.0025)

plt.subplot(3, 2, 1)
plt.plot(time, voltage, linewidth=1, color='black')

plt.subplot(3, 2, 3)
plt.plot(time, sigMF, linewidth=1, color='red')

plt.subplot(3, 2, 5)
plt.plot(time, sig, linewidth=1, color='blue')

plt.subplot(3, 2, 2)
plt.plot(time, filtered, linewidth=1, color='green')

#plt.subplot(1, 2, 2)
#plt.plot(freq, fourier, linewidth=1.5, color='blue')

plt.show()