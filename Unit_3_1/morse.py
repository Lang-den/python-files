import matplotlib.pyplot as plt

path = '../data_files/Secret_message.csv'

time_list = []
set1 = []
set2 = []

with open(path) as f:
    data = f.read().split('\n')

for line in data[1:]:
    vals = line.split(',')
    time_list.append(float(vals[0]))
    set1.append(float(vals[1]))
    set2.append(float(vals[2]))

plt.plot(time_list, set1, color=('darkred'))
plt.plot(time_list, set2, color=('purple'))
plt.title("Secret Message")
plt.xlabel("Time (in seconds)")
plt.ylabel("Decibals")
plt.grid('on')
plt.figlegend(
    ['Data A','Data C']
)
plt.show()
