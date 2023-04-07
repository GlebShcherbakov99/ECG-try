import time
import Adafruit_ADS1x15
import pandas as pd
import matplotlib.pyplot as plt
import csv

adc1 = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)
adc2 = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=0)

GAIN = 1

number_experiment = int(input())
print('Номер эксперимента: ' + number_experiment)
length_experiment = 500

i = 0
differ1 = []
differ2 = []
differ3 = []
differ4 = []
length = []

data = {}

while i < length_experiment:
    
    i += 1
    diff_1 = adc1.read_adc_difference(0, gain=GAIN, data_rate=128)
    diff_2 = adc1.read_adc_difference(3, gain=GAIN, data_rate=128)
    diff_3 = adc2.read_adc_difference(0, gain=GAIN, data_rate=128)
    diff_4 = adc2.read_adc_difference(3, gain=GAIN, data_rate=128)

    differ1.append(diff_1)
    differ2.append(diff_2)
    differ3.append(diff_3)
    differ4.append(diff_4)
    length.append(i)

plt.plot(length, differ1)
plt.plot(length, differ2)
plt.plot(length, differ3)
plt.plot(length, differ4)
plt.show()
plt.savefig('data №' + number_experiment + '.png')

data['diff1'] = differ1
data['diff2'] = differ2
data['diff3'] = differ3
data['diff4'] = differ4

DT = pd.DataFrame(data)
DT.to_csv('DATA №' + number_experiment + '.csv', sep=';', index=False)

time.sleep(0.05)

