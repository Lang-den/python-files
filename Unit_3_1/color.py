import matplotlib.pyplot as plt

path = "../data_files/light_data7.csv"

time = []
red = []
blue = []
green = []

with open(path) as f:
    data = f.read().strip().split('\n')


for line in data[1:]:
    vals = line.split(',')
    print(vals)
    time.append(float(vals[0]))
    red.append(float(vals[1]))
    green.append(float(vals[2]))
    blue.append(float(vals[3]))
    
fig, axes = plt.subplots(3,1, sharex='all')
plt.suptitle('Color in nanometers')
axes[0].plot(time, red, color='red')
axes[1].plot(time, green, color='green')
axes[2].plot(time, blue, color='blue')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency (nm)')
plt.figlegend([red, green, blue], ['red', 'green', 'blue'])
plt.show()