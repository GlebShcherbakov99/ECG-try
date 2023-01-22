print('-' *25)
print('simpletest STARTED')

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.fftpack as fftpack
import statsmodels.api as sm
from sqlalchemy import column
from scipy.fft import fft, fftfreq
from matplotlib.animation import FuncAnimation

print('... requirements OK')
import corefunc as cf
print('... corefunc OK')
df = cf.DFReadCSV('EXAMPLE.CSV')
print('... DFReadCSV OK')
time, voltage = cf.DFExtractData(df)
print('... DFExtractData OK')
sig = cf.LowessSig(time, voltage, 0.005)
print('... LowessSig OK')
freq, fft = cf.FFTSig(sig, 0.0025)
print('... FFTSig OK')
cf.DerivativeCheck(0, 0, 0, 0, 0)
print('... DerivativeCheck OK')

plt.figure(figsize=(16,8))

plt.subplot(3, 2, 1)
plt.plot(time, voltage, linewidth=1, color='black')
plt.grid(color='black', linewidth=0.5)
plt.ylabel("Signal")

plt.subplot(3, 2, 3)
plt.plot(time, voltage, linewidth=1, color='black')
plt.plot(time, sig, linewidth=2, color='red')
plt.grid(color='black', linewidth=0.5)
plt.ylabel("Signal+lowess")

plt.subplot(3, 2, 5)
plt.plot(time, sig, linewidth=2, color='green')
plt.grid(color='black', linewidth=0.5)
plt.ylabel("lowess")

plt.subplot(1, 2, 2)
plt.plot(freq, fft, linewidth=2, color='blue')
plt.grid(color='black', linewidth=0.5)
plt.xlim(-60, 60)
plt.title("FFT of signal after lowess")

plt.tight_layout(h_pad=2)
plt.tight_layout(w_pad=2)

plt.show()

print('simpletest COMPLETE, have fun!')
print('-' *25)