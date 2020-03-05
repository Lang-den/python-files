from tkinter import *
import gdx, matplotlib.pyplot as plt, numpy as np
#from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def start_recording():
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
    sensor.open_usb()
    #axis = fig.add_subplot(111)

    sensor.select_sensors([2,3])
    sensor.start(1000//samples)

    for _ in np.arange(0, seconds, step=1/samples):
        measurements = sensor.read()
        if measurements == None:
            break
        alist.append(measurements[0])
        clist.append(measurements[1])
        average.append(measurements)
        #samples_label.config(text=F"A Weighted Data: {measurements[0]}\n    C Weighted Data: {measurements[1]}")

    print(alist,clist)

    plt.plot(time, alist, color='red')
    plt.plot(time, clist, color='blue')
    plt.figlegend(['A Weighted Data', 'C Weighted Data'])
    plt.title('Sound Measured Over Time')
    plt.xlabel('Time(s)')
    plt.ylabel('Frequency(dB)')
    plt.xticks(time)
    plt.grid()
    plt.show()
    
    sensor.stop()
    sensor.close()


root = Tk()


seconds_label = Label(root, text='How many seconds?')
seconds_label.pack()
seconds_entry = Entry(root)
seconds_entry.pack()

samples_label = Label(root, text='How many samples/second?')
samples_label.pack()
samples_entry = Entry(root)
samples_entry.pack()

start_button = Button(root, text='Start Recording', command=start_recording)
start_button.pack()

sensor = gdx.gdx()

root.mainloop()