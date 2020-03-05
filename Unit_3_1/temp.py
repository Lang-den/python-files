import matplotlib.pyplot as plt

path = '../data_files/raw_data_311.csv'

time_list = []
temp1_list = []
temp2_list = []

with open(path) as f:
    data = f.read().split('\n')

for line in data[1:]:
    vals = line.split(',')
    time_list.append(float(vals[0]))
    temp1_list.append(float(vals[1]))
    temp2_list.append(float(vals[2]))

plt.plot(time_list, temp1_list, color=('darkred'))
plt.plot(time_list, temp2_list, color=('purple'))
plt.title("Time vs. Temperature")
plt.xlabel("Time (in seconds)")
plt.ylabel("Temperature (in celsius)")
plt.grid('on')
plt.figlegend(
    ['Ice Water','Unknown Substance']
)
plt.show()
