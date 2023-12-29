#!/usr/bin/env python3

import sys
from tkinter import *
from time import gmtime, strftime

#display date & time in window
def Clock():
    curr_time = strftime("%Y/%m/%d, %T")
    curr_time_utc = strftime("%Y/%m/%d, %T", gmtime())
    clock.config(text=curr_time)
    clock2.config(text=curr_time_utc)
    clock.after(100,Clock)

#making window and title
window=Tk()
window.title('Local & UTC Clocks')

#giving name to clocks and style
message = Label(window, font=("times",30,"bold"), text="Local", fg="black")
message.grid(row=0,column=0)
clock = Label(window, font=("times",40,"bold"),fg="purple")
clock.grid(row=1,column=0)
message = Label(window, font=("times",30,"bold"), text="UTC", fg="black")
message.grid(row=2,column=0)
clock2 = Label(window, font=("times",40,"bold"),fg="purple")
clock2.grid(row=3,column=0)
Clock()
mainloop()
