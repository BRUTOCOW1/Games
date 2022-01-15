from pydoc import text
import tkinter as tk
from tkinter import *
from datetime import date
# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it 
# at label widget
  
def printInput():
    mon = inputmonth.get(1.0, "end-1c")
    da = inputday.get(1.0,"end-1c")
    yea = inputyear.get(1.0, "end-1c")
    dat = date.today()
    d3 = dat.strftime("%m/%d/%y")
    years = int('20'+d3.split("/")[2]) - int(yea)
    months = int(d3.split("/")[0]) - int(mon)
    days = int(d3.split("/")[1]) - int(da)
    age = years + (months/12) + (days/12/30)
    lbl.config(text = "Age: "+str(age))
    lb.config(text="Percent of 80: " +str(age/80*100))
  
# TextBox Creation
inputmonth = tk.Text(frame,
                   height = 2,
                   width = 10)
inputmonth.grid(column=1,row=1)
inputday = tk.Text(frame,
                   height = 2,
                   width = 10)
inputday.grid(column=2,row=1)
inputyear = tk.Text(frame,
                   height = 2,
                   width = 10)
inputyear.grid(column=3,row=1)
lbl = tk.Label(frame, text = "")
lbl.grid(column=4,row=1)
lb = tk.Label(frame, text = "")
lb.grid(column=5,row=1)

mond = tk.Label(frame,text="month")
mond.grid(column=1,row=2)
dayd = tk.Label(frame,text="day")
dayd.grid(column=2,row=2)
yeard = tk.Label(frame,text="year")
yeard.grid(column=3,row=2)

# Button Creation
printButton = tk.Button(frame,
                        text = "Print", 
                        command = printInput)
printButton.grid(column=4,row=2)
# Label Creation

frame.mainloop()