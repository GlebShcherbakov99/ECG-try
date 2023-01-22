import corefunc as cf
import Adafruit_ADS1x15
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.fftpack as fftpack
import statsmodels.api as sm
import time
from sqlalchemy import column
from scipy.fft import fft, fftfreq
print('requirements OK ...')

adc = Adafruit_ADS1x15.ADS1015(0x48, busnum=1)
GAIN = 1
print('ADS1015 OK ...')
print('Start ...')

t0 = 0
value_list = []
time_list = []
timesleep = 0.005

exp_time = int(input('Введите время эксперимента, с '))
n_id = str(input('Number of experiment '))
name_id = 'first exp data/first exp #' + n_id + '.csv'

while t0 < exp_time:
    value = round(adc.read_adc_difference(0, gain=GAIN, data_rate=3300) / 500, 2)
    print('Muscular activity = {0}'.format(value))
    value_list.append(value)
    time.sleep(timesleep)
    t0 += timesleep
    time_list.append(t0)

sig = cf.LowessSig(time_list, value_list, 0.01)
print('Lowess OK ...')
freq, fft = cf.FFTSig(value_list, len(value_list)/time_list[-1])
#freq, fft = cf.FFTSig(value_list, 0.0033)
print('FFT OK ...')

df = pd.DataFrame({'time': time_list,
		   'voltage': value_list,
		   'lowess': sig})

cf.CSVFileSave(df, name_id)
print('File Save OK ...')

plt.figure(figsize=(16,8))

plt.subplot(3, 1, 1)
plt.plot(time_list, value_list, linewidth=1, color='black')
plt.grid(color='black', linewidth=0.5)
plt.ylabel("Signal")

plt.subplot(3, 1, 2)
plt.plot(time_list, sig, linewidth=2, color='red')
plt.grid(color='black', linewidth=0.5)
plt.ylabel("Lowess")

plt.subplot(3, 1, 3)
plt.plot(freq, fft, linewidth=2, color='blue')
plt.grid(color='black', linewidth=0.5)
plt.title("FFT of signal after lowess")

plt.show()
plt.savefig('first exp data/pic #' + n_id + '.png')
