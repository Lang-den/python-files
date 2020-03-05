import matplotlib.pyplot as plt

path = '../data_files/weather.csv'

actMeanTemp = []
actMinTemp = []
actMaxTemp = []
actPrecip = []
recMinTemp = []
recMaxTemp = []

with open(path) as f:
    data = f.read().strip().split('\n')

for line in data[1:]:
    vals = line.split(',')
    actMeanTemp.append(int(vals[1]))
    actMinTemp.append(int(vals[2]))
    actMaxTemp.append(int(vals[3]))
    actPrecip.append(float(vals[12]))
    recMinTemp.append(int(vals[6]))
    recMaxTemp.append(int(vals[7]))

fig, axes = plt.subplots(2, 3)
axes[0][0].plot(actMeanTemp, color='green')
axes[0][1].plot(actMinTemp, color='blue')
axes[0][2].plot(actMaxTemp, color='red')
axes[1][0].plot(actPrecip, color='lightblue')
axes[1][1].plot(recMinTemp, color='darkblue')
axes[1][2].plot(recMaxTemp, color='blanchedalmond')

fig.canvas.set_window_title('Weather')

axes[0][0].title.set_text('Actual Mean Temp.')
axes[0][1].title.set_text('Actual Min. Temp.')
axes[0][2].title.set_text('Actual Max. Temp.')
axes[1][0].title.set_text('Actual Precip.')
axes[1][1].title.set_text('Record Min. Temp.')
axes[1][2].title.set_text('Record Max. Temp.')

for ax in axes[0][:]:
    ax.grid()
for ax in axes[1][:]:
    ax.grid()

plt.show()