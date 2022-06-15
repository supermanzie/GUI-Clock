from tkinter import *
from tkinter.ttk import *
import datetime

#window
clockgui = Tk()
clockgui.title('Digital Clock')
clockgui.geometry('400x200')
clockgui.configure(bg='black')

timeLabel = Label(font = 'LucidaBright 50 bold', foreground = 'green', background = 'black')
timeLabel.pack(anchor='center')
dateLabel = Label(font = 'calibri 25', foreground = 'green', background = 'black')
dateLabel.pack(anchor='s')

#clock
def clock():
    date_time = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    date,time = date_time.split()
    hour,minutes,seconds =  time.split(':')
    timeLabel.config(text = time)
    dateLabel.config(text = date)
    timeLabel.after(1000, clock)
clock()
clockgui.mainloop()