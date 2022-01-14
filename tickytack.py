from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from tkmacosx import Button

root = Tk()
root.title('tic-tac-toe')

clicked = True
count = 0
root.configure(bg='blue')

xx = []
oo = []

def b_click(b,b1):
    global clicked, count
    global xx,oo
    message = "hello"
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        b["bg"] = "blue"
        clicked = False
        count+=1
        xx.append(b1)
        lost = "X"
        squad = xx
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        b["bg"] = "red"
        clicked = True
        count+=1
        oo.append(b1)
        lost = "O"
        squad = oo
    else:
        messagebox.showerror("Fuck You Bitch", "Fuck You Bitch\n Fuck You Bitch")
        return 0
    check(squad,lost)

black = (0,0,0)

b1 = Button(root, text = " ", font=("Helvetica",20),height=60,width=120,bg='Grey', command= lambda: b_click(b1, 1))
b2 = Button(root, text = " ", font=("Helvetica",20),height=60,width=120,bg="Grey",command=lambda: b_click(b2,2))
b3 = Button(root, text = " ", font=("Helvetica",20),height=60,width=120,bg="Grey",command=lambda: b_click(b3,3))
b4 = Button(root, text = " ", font=("Helvetica",20),height=60,width=120,bg="Grey",command=lambda: b_click(b4,4))
b5 = Button(root, text = " ", font=("Helvetica",20),height=60,width=120,bg="Grey",command=lambda: b_click(b5,5))
b6 = Button(root, text = " ", font=("Helvetica",20),height=60,width=120,bg="Grey",command=lambda: b_click(b6,6))
b7 = Button(root, text = " ", font=("Helvetica",20),height=60,width=120,bg="Grey",command=lambda: b_click(b7,7))
b8 = Button(root, text = " ", font=("Helvetica",20),height=60,width=120,bg="Grey",command=lambda: b_click(b8,8))
b9 = Button(root, text = " ", font=("Helvetica",20),height=60,width=120,bg="Grey",command=lambda: b_click(b9,9))

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

winner = False

def disable_all_buttons():
    b1.configure(state=DISABLED)
    b2.configure(state=DISABLED)
    b3.configure(state=DISABLED)
    b4.configure(state=DISABLED)
    b5.configure(state=DISABLED)
    b6.configure(state=DISABLED)
    b7.configure(state=DISABLED)
    b8.configure(state=DISABLED)
    b9.configure(state=DISABLED)



def check(lis,lost):
    global winner
    if 1 in lis and ((2 in lis and 3 in lis) or (4 in lis and 7 in lis ) or (5 in lis and 9 in lis)):
        winner = True
        messagebox.showinfo("Yompeea", lost+ " Wins!")
    elif 2 in lis and 5 in lis and 8 in lis:
        winner = True
        messagebox.showinfo("Yompeea", lost+ " Wins!")
    elif 3 in lis and ((6 in lis and 9 in lis) or (5 in lis and 7 in lis)):
        winner = True
        messagebox.showinfo("Yompeea", lost+ " Wins!")
    elif (4 in lis and 5 in lis and 6 in lis) or (7 in lis and 8 in lis and 9 in lis):
        winner = True
        messagebox.showinfo("Yompeea", lost+ " Wins!")
def reset():
    global xx,oo
    b1.configure(text = " ", font=("Helvetica",20),height=60,width=120,bg='Grey', command= lambda: b_click(b1, 1))
    b2.configure(text = " ", font=("Helvetica",20),height=60,width=120,bg="Grey",command=lambda: b_click(b2,2))
    b3.configure(text = " ", font=("Helvetica",20),height=60,width=120,bg="Grey",command=lambda: b_click(b3,3))
    b4.configure(text = " ", font=("Helvetica",20),height=60,width=120,bg="Grey",command=lambda: b_click(b4,4))
    b5.configure(text = " ", font=("Helvetica",20),height=60,width=120,bg="Grey",command=lambda: b_click(b5,5))
    b6.configure(text = " ", font=("Helvetica",20),height=60,width=120,bg="Grey",command=lambda: b_click(b6,6))
    b7.configure(text = " ", font=("Helvetica",20),height=60,width=120,bg="Grey",command=lambda: b_click(b7,7))
    b8.configure(text = " ", font=("Helvetica",20),height=60,width=120,bg="Grey",command=lambda: b_click(b8,8))
    b9.configure(text = " ", font=("Helvetica",20),height=60,width=120,bg="Grey",command=lambda: b_click(b9,9))
    xx = []
    oo = []
  

  
# Button Creation
printButton = tk.Button(root, height=1,width=2,
                        text = "Reset", 
                        command = reset)
printButton.grid(row=3,column=1)
  


root.mainloop()