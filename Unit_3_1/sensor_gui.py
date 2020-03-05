from tkinter import *
import gdx, matplotlib.pyplot as plt, numpy as np
#from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


sensor = gdx.gdx()
sensor.open_usb()
sensor.select_sensors([2,3])

def start_recording():
    ax.clear()
    seconds = int(seconds_entry.get())
    samples = int(samples_entry.get())
    alist = []
    clist = []
    average = []
    time = []
    #fig = Figure(dpi=100)
    #canvas = FigureCanvasTkAgg(fig, master=root)
    #canvas.draw()
    #canvas.get_tk_widget().pack()
    time = np.arange(0, seconds, step=1/samples)
    #axis = fig.add_subplot(111)

    
    chart = FigureCanvasTkAgg(fig, root)
    chart.get_tk_widget().grid(row=0, column=1, rowspan=20)

    sensor.start(1000//samples)

    for _ in np.arange(0, seconds, step=1/samples):
        measurements = sensor.read()
        if measurements == None:
            break
        alist.append(measurements[0])
        clist.append(measurements[1])
        average.append((measurements[0]+measurements[1])/2)
        #samples_label.config(text=F"A Weighted Data: {measurements[0]}\n    C Weighted Data: {measurements[1]}")

    ax.plot(time, alist, color='red')
    ax.plot(time, clist, color='blue')
    ax.plot(time, average, color='green')
    ax.legend(['A Weighted Data', 'C Weighted Data', 'Average of Data'])
    ax.set_title('Sound Measured Over Time')
    ax.set_xlabel('Time(s)')
    ax.set_ylabel('Frequency(dB)')
    ax.set_xticks(time)
    ax.grid(b=True)
    #plt.ion()
    
    sensor.stop()
    #sensor.close()


root = Tk()


seconds_label = Label(root, text='How many seconds?')
seconds_label.grid(column=0, row=0)
seconds_entry = Entry(root)
seconds_entry.grid(column=0, row=1)

samples_label = Label(root, text='How many samples/second?')
samples_label.grid(column=0, row=2)
samples_entry = Entry(root)
samples_entry.grid(column=0, row=3)

start_button = Button(root, text='Start Recording', command=start_recording)
start_button.grid(column=0,row=4)

fig, ax = plt.subplots()

root.mainloop()