import sys
sys.insert(0, './lib')
import tkinter as tk
from tkinter import commondialog
from tkinter.commondialog import Dialog
from tkinter import Canvas
from tkinter import *
from tkinter.ttk import *

# class Game(tk.Frame):
    # def __init__(self):
    #     tk.Frame.__init__(self)
    #     self.grid()
    #     self.master.title('My game of Chance')
        
main = tk.Tk()
        
canvas = tk.Canvas(main, height= 700, width=700, bg='black')
canvas.pack()

frame = tk.Frame(main, bg='red')
frame.place(relheight=0.5, relwidth=0.5 )

restart_message = tk.messagebox.askquestion(main, title=start_game, message="choice" command=restart)
restart_message.pack()
main.mainloop()

