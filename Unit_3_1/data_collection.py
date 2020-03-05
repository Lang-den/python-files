import gdx
import matplotlib.pyplot as plt
import numpy as np

sensor = gdx.gdx()
sensor.open_usb()
alist = []
clist = []
time = []

sec_num = int(input('\n How many seconds of data would you like to record?: '))
time = np.arange(0, sec_num, step=0.5)

sensor.select_sensors([2,3])
sensor.start(500)

for i in range(sec_num*2):
    measurements = sensor.read()
    if measurements == None:
        break
    alist.append(measurements[0])
    clist.append(measurements[1])
    print(F"A Weighted Data: {measurements[0]}\n    C Weighted Data: {measurements[1]}")

sensor.stop()
sensor.close()

plt.plot(time, alist, color='red')
plt.plot(time, clist, color='blue')
plt.figlegend(['A Weighted Data', 'C Weighted Data'])
plt.title('Sound Measured Over Time')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (dB)')
plt.xticks(time)
plt.grid()
plt.show()