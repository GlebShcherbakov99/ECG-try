import time
import Adafruit_ADS1x15
import csv

adc1 = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)
adc2 = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=0)

GAIN = 1

fieldnames = ["frame", "diff1", "diff2", "diff3", "diff4"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

print('Press Ctrl-C to quit...')

while True:
    
    with open('data.csv', 'a') as csv_file:

        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "frame": frames,
            "diff1": diff_1,
            "diff2": diff_2,
            "diff3": diff_3,
            "diff4": diff_4
        }

        csv_writer.writerow(info)
        print(frame, diff1, diff2, diff3, diff4)

        frames += 1
                
        diff_1 = adc1.read_adc_difference(0, gain=GAIN, data_rate=128)
        diff_2 = adc1.read_adc_difference(3, gain=GAIN, data_rate=128)
        diff_3 = adc2.read_adc_difference(0, gain=GAIN, data_rate=128)
        diff_4 = adc2.read_adc_difference(3, gain=GAIN, data_rate=128)

time.sleep(0.1)
